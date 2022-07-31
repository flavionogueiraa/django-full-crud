def init_view_script(model_name, snake_model_name):
    return f"""from .{snake_model_name}_create_view import {model_name}CreateView
from .{snake_model_name}_delete_view import {model_name}DeleteView
from .{snake_model_name}_detail_view import {model_name}DetailView
from .{snake_model_name}_list_view import {model_name}ListView
from .{snake_model_name}_update_view import {model_name}UpdateView

__all__ = [
    {model_name}CreateView,
    {model_name}DeleteView,
    {model_name}DetailView,
    {model_name}ListView,
    {model_name}UpdateView,
]
"""
