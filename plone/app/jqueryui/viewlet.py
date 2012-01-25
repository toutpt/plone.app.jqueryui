from zope import component
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry

from plone.app.jqueryui.interfaces import IJQueryUIPlugins
from plone.app.jqueryui.utils import get_datepicker_date_format

# this list was generated from jqueryui 1.8rc3
JQUERYUI_LANGUAGES = (
    'af', 'ar', 'az', 'bg', 'bs', 'ca', 'cs', 'da', 'de', 'el', 'en-GB', 'eo',
    'es', 'et', 'eu', 'fa', 'fi', 'fr-CH', 'fr', 'he', 'hr', 'hu', 'hy', 'id',
    'is', 'it', 'ja', 'ko', 'lt', 'lv', 'ms', 'nl', 'no', 'pl', 'pt-BR', 'ro',
    'ru', 'sk', 'sl', 'sq', 'sr', 'sr-SR', 'sv', 'th', 'tr', 'uk', 'vi',
    'zh-CN', 'zh-HK', 'zh-TW',
)


class L10nDatepicker(ViewletBase):

    def jq_language(self):
        language = self.request.get('LANGUAGE', '')
        if '-' in language:
            # normalize combined language code
            parts = language.split('-')
            language = "%s-%s" % (parts[0], parts[1].upper())
            if language in JQUERYUI_LANGUAGES:
                return language
            else:
                # If the combined language doesn't exist in jqueryui
                # check only the first part.
                language = language.split('-')[0]
        if language in JQUERYUI_LANGUAGES:
            return language
        # Return empty string if the language is not supported
        # by jqueryui so the default this.regional[''] of the datepicker
        # plugin is used.
        return ''

    def update(self):
        self.jq_date_format = get_datepicker_date_format(self.request)

    def render(self):
        registry = component.queryUtility(IRegistry)
        if registry is None:
            return u''
        record = registry.forInterface(IJQueryUIPlugins, None)
        if record is None:
            return u''
        if not record.ui_datepicker:
            return u''
        return u"""<script type="text/javascript">
        jQuery(function($){
            $.datepicker.setDefaults(
                jQuery.extend($.datepicker.regional['%s'],
                {dateFormat: '%s'}));
        });
        </script>""" % (self.jq_language(), self.jq_date_format)
