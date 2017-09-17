from re import compile
from django.conf import settings
from django.template.loader import render_to_string


# We want to be looking at an app in the admin, not the admin's list page.
PATH_MATCHER = compile(r"^/admin/\w+")


class ChosenAdminMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

        self.include_flag = "<!-- CHOSEN INCLUDED -->"
        self.js_template = "chosenadmin/js/chosen.jquery.min.js"
        self.css_template = "chosenadmin/css/chosen.min.css"
        self.chosen_sprites = ['chosen-sprite.png', 'chosen-sprite@2x.png']

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_template_response(request, response)

    def _match(self, request, response):
        """Match all requests/responses that satisfy the following conditions:

        * An Admin App; i.e. the path is something like /admin/some_app/
        * The ``include_flag`` is not in the response's content

        """
        is_html = 'text/html' in response.get('Content-Type', '')
        if is_html and hasattr(response, 'rendered_content'):
            correct_path = PATH_MATCHER.match(request.path) is not None
            not_included = self.include_flag not in response.rendered_content
            return correct_path and not_included
        return False

    def _chosen_css(self):
        """Read the minified CSS file including STATIC_URL in the references
        to the sprite images."""
        css = render_to_string(self.css_template, {})
        for sprite in self.chosen_sprites:  # rewrite path to sprites in the css
            css = css.replace(sprite, settings.STATIC_URL + "img/" + sprite)
        return css

    def _chosen_js(self):
        """Read the minified jquery plugin file."""
        return render_to_string(self.js_template, {})

    def _embed(self, request, response):
        """Embed Chosen.js directly in html of the response."""
        if self._match(request, response):
            # Render the <link> and the <script> tags to include Chosen.
            head = render_to_string(
                "chosenadmin/_head_css.html",
                {"chosen_css": self._chosen_css()}
            )
            body = render_to_string(
                "chosenadmin/_script.html",
                {"chosen_js": self._chosen_js()}
            )

            # Re-write the Response's content to include our new html
            content = response.rendered_content
            content = content.replace('</head>', head)
            content = content.replace('</body>', body)
            response.content = content
        return response

    def __call__(self, request):
        response = self.get_response(request)
        return self._embed(request, response)
