// Generated by CoffeeScript 1.6.2
(function() {
    (function($) {
        return $.widget('IKS.hallowagtaildoclink', {
            options: {
                uuid: '',
                editable: null
            },
            populateToolbar: function(toolbar) {
                var button;
                var widget;

                widget = this;
                button = $('<span class="' + this.widgetName + '"></span>');
                button.hallobutton({
                    uuid: this.options.uuid,
                    editable: this.options.editable,
                    label: 'Documents',
                    icon: 'icon-doc-full',
                    command: null
                });
                toolbar.append(button);
                return button.on('click', function(event) {
                    var lastSelection;

                    lastSelection = widget.options.editable.getSelection();
                    return ModalWorkflow({
                        url: window.chooserUrls.documentChooser,
                        onload: DOCUMENT_CHOOSER_MODAL_ONLOAD_HANDLERS,
                        responses: {
                            documentChosen: function(docData) {
                                var a;

                                a = document.createElement('a');
                                a.setAttribute('href', docData.url);
                                a.setAttribute('data-id', docData.id);
                                a.setAttribute('data-linktype', 'document');
                                if ((!lastSelection.collapsed) && lastSelection.canSurroundContents()) {
                                    lastSelection.surroundContents(a);
                                } else {
                                    a.appendChild(document.createTextNode(docData.title));
                                    lastSelection.insertNode(a);
                                }

                                return widget.options.editable.element.trigger('change');
                            }
                        }
                    });
                });
            }
        });
    }(jQuery));
}).call(this);
