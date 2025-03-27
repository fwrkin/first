from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from catalog.services import get_products_from_cache, get_products_by_category


class DeleteProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if product.owner != request.user:
            return HttpResponseForbidden('Вы можете удалять только свои продукты')

        if not request.user.has_perm('catalog.can_delete_product') and product.owner != request.user:
            return HttpResponseForbidden('У вас нет права для удаления продукта')

        product.delete()

        return redirect('catalog:products_list')


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if product.owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет права для снятия продукта с публикации')

        product.is_published = False
        product.save()

        return redirect('catalog:products_detail', pk=product.id)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_initial(self):
        initial = super().get_initial()
        initial["owner"] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')


class ProductListView(LoginRequiredMixin,ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()

class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product


class ProductsByCategoryView(ListView):
    model = Product
    template_name = 'catalog/products_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs.get('category')
        context['products'] = get_products_by_category(category)
        context['category'] = category
        return context
