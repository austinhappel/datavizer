/*jslint devel: true, browser: true, nomen: true, maxerr: 50, indent: 4 */
/*global jQuery, $, _ */

(function (global) {
    "use strict";

    var $dataset = $('#id_dataset');
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
