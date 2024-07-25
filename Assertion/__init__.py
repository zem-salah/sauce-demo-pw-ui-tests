import os
import inspect
import importlib


def init_assertions_module(context):
    """
    This method dynamically initialize assertion classes and execute
    a set_context method to pass the behave context to them. This is done
    to avoid passing context object each time when doing an assertion.

    We want to avoid : AssertThat(Page(context, ...)).<do some check>

    Args:
        context: The context in which to initialize the actions.
    """
    actions_path = os.path.dirname(os.path.abspath(__file__))
    module_name = os.path.basename(actions_path)

    for filename in os.listdir(actions_path):
        if filename.endswith('.py') and filename != '__init__.py':
            module = importlib.import_module(
                f"{module_name}.{filename[:-3]}")
            for name, obj in inspect.getmembers(module, inspect.isclass):
                # If the class has a 'should_init' attribute set to True
                if hasattr(obj, 'should_init') and obj.should_init \
                        and hasattr(obj, 'set_context'):
                    obj.set_context(context)
