import functools


class Notify:
    def __init__(self):
        self.events = {}

    def register(self, event, component):
        if event not in self.events:
            self.events[event] = []

        if component in self.events[event]:
            # no-op if component already exists
            return

        self.events[event].append(component)

    def trigger(self, event, *args, **kwargs):
        if event not in self.events:
            raise Exception(f"Event {event} not found.")

        for component in self.events[event]:
            fn = getattr(component, f"handle_{event}", None)
            if not fn:
                raise Exception(
                    f"Method handle_{event} not found in {component}"
                )
            fn(event, *args, **kwargs)


NOTIFY = Notify()


class EventHandler:
    def __init__(self, event):
        self.event = event

    def register_component(self, cls: object, *args, **kwargs):
        component = cls(*args, **kwargs)
        NOTIFY.register(self.event, component)
        return component

    def __call__(self, *param_args, **param_kwargs):
        if len(param_args) == 1:
            cls = param_args[0]

            @functools.wraps(cls)
            def wrapper(*args, **kwargs):
                return self.register_component(cls, *args, **kwargs)
            return wrapper
        return self.register_component(param_args, *param_args, **param_kwargs)
