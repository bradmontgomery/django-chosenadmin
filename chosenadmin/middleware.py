from re import compile
from django.conf import settings
from django.template.loader import render_to_string


# We want to be looking at an app in the admin, not the admin's list page.
PATH_MATCHER = compile(r"^/admin/\w+")


class ChosenAdminMiddleware(object):

    def __init__(self, *args, **kwargs):

        self.include_flag = getattr(
            settings,
            'CHOSENADMIN_INCLUDE_FLAG',
            "<!-- CHOSEN INCLUDED -->"
        )
        self.minified_css = getattr(settings, 'CHOSENADMIN_MIN_CSS', True)
        self.minified_js = getattr(settings, 'CHOSENADMIN_MIN_JS', True)

    def _match(self, request, response):
        """Match all requests/responses that satisfy the following conditions:

        * An Admin App; i.e. the path is something like /admin/some_app/
        * The ``include_flag`` is not in the response's content

        """
        correct_path = PATH_MATCHER.match(request.path) is not None
        not_included = self.include_flag not in response.rendered_content
        return correct_path and not_included

    def _chosen_css(self, minified=True):
        """Read the minified CSS file including STATIC_URL in the references
        to the sprite images."""
        file = "chosen.min.css" if minified else "chosen.css"
        path = "chosenadmin/css/{0}".format(file)
        css = render_to_string(path, {})
        for sprite in ['chosen-sprite.png', 'chosen-sprite@2x.png']:
            css = css.replace(sprite, settings.STATIC_URL + "img/" + sprite)
        return css

    def _chosen_js(self, minified=True):
        """Read the minified jquery plugin file."""
        file = "chosen.jquery.min.js" if minified else "chosen.jquery.js"
        path = "chosenadmin/js/{0}".format(file)
        return render_to_string(path, {})

    def process_template_response(self, request, response):
        """Embed Chosen.js directly in html of the response."""

        if self._match(request, response):
            # Render the <link> and the <script> tags to include Chosen.
            head = render_to_string(
                "chosenadmin/_head_css.html",
                {"minified_css": self._chosen_css(minified=self.minified_css)}
            )
            body = render_to_string(
                "chosenadmin/_script.html",
                {"chosen_js": self._chosen_js(minified=self.minified_js)}
            )

            # Re-write the Response's content to include our new html
            content = response.rendered_content
            content = content.replace('</head>', head)
            content = content.replace('</body>', body)
            response.content = content

        return response
