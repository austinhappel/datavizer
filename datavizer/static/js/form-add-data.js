/*jslint devel: true, browser: true, nomen: true, maxerr: 50, indent: 4 */
/*global jQuery, $, _ */

(function (global) {
    "use strict";

    var $dataset = $('#id_dataset'),
        $submit = $('#form-add-data-btn-submit');

    function updateDataField() {
        var data = {};

        $('#data-fields input').each(function () {
            var $this = $(this),
                key = $this.attr('id'),
                value = $this.val();
            data[key] = value;
        });

        $('#id_data')
            .empty()
            .text(JSON.stringify(data, 4));
    }

    function bindDataFieldChanges() {
        var $fields = $('#data-fields input');

        $fields.on('change', function (e) {
            updateDataField();
        });
    }
    /**
     * On dataset select menu change, add fields based on the new dataset requested.
     * @return {undefined}
     */
    $dataset.change(function () {
        var datasetId = $('#id_dataset').find('option:selected').val(),
            dataFieldTemplate = _.template($('#data-field-template').html());

        function ajaxSuccess(data) {
            var $dataFields = $('#data-fields');

            if (data.res === 'ok') {
                $dataFields.empty();
                _.each(data.schema, function (field, name) {
                    $dataFields.append(dataFieldTemplate({fieldName: name}));
                });
                bindDataFieldChanges();
            }
        }

        function ajaxError(jqXHR) {
            console.log('error');
            console.log(jqXHR);
        }

        $.ajax({
            url: '/data/get_dataset_schema/' + datasetId + '/',
            success: ajaxSuccess,
            error: ajaxError
        });
    });
}(this));
