from zope.interface import Interface
from zope import schema

class IJqueryUILayer(Interface):
    """Browser layer"""

class IJQueryUIPlugins(Interface):
    
    ui_core = schema.Bool(title=u"Core",
                       description=u"The core of jQuery UI, required for all interactions and widgets.",
                       required=False,default=False)
    
    ui_widget = schema.Bool(title=u"Widget",
                         description=u"",required=False,default=False)

    ui_mouse = schema.Bool(title=u"Mouse",
                         description=u"",required=False,default=False)

    ui_position = schema.Bool(title=u"Position",
                         description=u"",required=False,default=False)

    ui_draggable = schema.Bool(title=u"Draggable",
                         description=u"",required=False,default=False)

    ui_droppable = schema.Bool(title=u"Droppable",
                         description=u"",required=False,default=False)

    ui_resizable = schema.Bool(title=u"Resizable",
                         description=u"",required=False,default=False)

    ui_selectable = schema.Bool(title=u"Selectable",
                         description=u"",required=False,default=False)

    ui_sortable = schema.Bool(title=u"Sortable",
                         description=u"",required=False,default=False)

    ui_accordion = schema.Bool(title=u"Accordion",
                         description=u"",required=False,default=False)

    ui_autocomplete = schema.Bool(title=u"Autocomplete",
                         description=u"",required=False,default=False)

    ui_button = schema.Bool(title=u"Button",
                         description=u"",required=False,default=False)

    ui_dialog = schema.Bool(title=u"Dialog",
                         description=u"",required=False,default=False)

    ui_slider = schema.Bool(title=u"Slider",
                         description=u"",required=False,default=False)

    ui_tabs = schema.Bool(title=u"Tabs",
                         description=u"",required=False,default=False)

    ui_datepicker = schema.Bool(title=u"Date picker",
                         description=u"",required=False,default=False)

    ui_progressbar = schema.Bool(title=u"Progress bar",
                         description=u"",required=False,default=False)

    effects_core = schema.Bool(title=u"Effects 'core'",
                         description=u"",required=False,default=False)

    effects_blind = schema.Bool(title=u"Effects 'blind'",
                         description=u"",required=False,default=False)

    effects_bounce = schema.Bool(title=u"Effects 'bounce'",
                         description=u"",required=False,default=False)

    effects_clip = schema.Bool(title=u"Effects 'clip'",
                         description=u"",required=False,default=False)

    effects_drop = schema.Bool(title=u"Effects 'drop'",
                         description=u"",required=False,default=False)

    effects_explode = schema.Bool(title=u"Effects 'explode'",
                         description=u"",required=False,default=False)

    effects_fade = schema.Bool(title=u"Effects 'fade'",
                         description=u"",required=False,default=False)

    effects_fold = schema.Bool(title=u"Effects 'fold",
                         description=u"",required=False,default=False)

    effects_highlight = schema.Bool(title=u"Effects 'highlight'",
                         description=u"",required=False,default=False)

    effects_pulsate = schema.Bool(title=u"Effects 'pulsate'",
                         description=u"",required=False,default=False)

    effects_scale = schema.Bool(title=u"Effects 'scale'",
                         description=u"",required=False,default=False)

    effects_shake = schema.Bool(title=u"Effects 'shake'",
                         description=u"",required=False,default=False)

    effects_slide = schema.Bool(title=u"Effects 'slide'",
                         description=u"",required=False,default=False)

    effects_transfer = schema.Bool(title=u"Effects 'transfer'",
                         description=u"",required=False,default=False)
    
