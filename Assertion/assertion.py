from robber import expect, BadExpectation

from page_object.page_factory import PageFactory


class AssertThat:

    should_init = True
    context = None

    @classmethod
    def set_context(cls, context):
        cls.context = context

    class _Page:

        def __init__(self, context, expected_page_pretty_name):
            self.expected_page_pretty_name = expected_page_pretty_name
            self.expected_page_object = PageFactory(context)(
                expected_page_pretty_name)
            self.actual_page = context.current_page

        def is_visible(self):
            try:
                expect(self.expected_page_object.is_visible()).to.be.true()
            except BadExpectation as e:
                e.message = f'Page {self.expected_page_pretty_name} is not ' \
                            f'visible'
                raise e

        def is_current_page(self):
            expect(isinstance(
                self.actual_page, type(self.expected_page_object)
            )).to.be.true()

    @classmethod
    def Page(cls, expected_page_pretty_name):
        return cls._Page(cls.context, expected_page_pretty_name)
