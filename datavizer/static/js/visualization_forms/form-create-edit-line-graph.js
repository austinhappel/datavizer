/*jslint devel: true, browser: true, nomen: true, maxerr: 50, indent: 4 */
/*global jQuery, $, _*/

(function (global) {
    "use strict";

    var legendNum = 0,
        LegendCreator,
        $container = $('#legends'),
        $datasets = $('#id_datasets'),
        $form = $('#form-create-visualization'),
        getSchemaBaseUrl = '/data/get_dataset_schema/',
        datasetOptions = global.dataset_options;


    LegendCreator = function () {
        legendNum += 1;

        var legendFormTemplate = _.template($('#legend-template').html()),
            renderedTemplate = legendFormTemplate({legendNum: legendNum}),
            $legendForm,
            datasetOptionHtml = '';

        _.each(datasetOptions, function (option) {
            datasetOptionHtml += '<option value="' + option.id + '">' + option.name + '</option>';
        });

        $container.append(renderedTemplate);
        $legendForm = $container.find('#legend_' + legendNum);
        $legendForm
            .find('#legend_' + legendNum + '_dataset')
            .append(datasetOptionHtml);

        function getDatasetFieldsError(jqXHR) {
            console.log('error:');
            console.log(jqXHR);
        }

        // on success, rebuild select boxes with new schema options.
        function getDatasetFieldsSuccess(data) {
            if (data.res !== 'ok') {
                getDatasetFieldsError(data);
                return;
            }

            console.log('SUCCESS');

            var options = '';

            _.each(data.schema, function (type, name) {
                options += '<option value="' + name + '">' + name + '</option>\n';
            });

            $legendForm
                .find('#legend_' + legendNum + '_field_for_x_value, #legend_' + legendNum + '_field_for_y_value')
                .html(options);

            $legendForm.find('.legend-details').show();
        }

        function getDatasetFields(datasetId, funcSuccess, funcError) {
            console.log('ajax: ' + getSchemaBaseUrl + datasetId);
            $.ajax({
                url: getSchemaBaseUrl + datasetId,
                success: getDatasetFieldsSuccess,
                error: getDatasetFieldsError
            });
        }

        // hide details section until a dataset has been chosen.
        $legendForm.find('.legend-details').hide();

        // bind events
        $legendForm
            .find('#legend_' + legendNum + '_dataset')
            .change(function () {
                var datasetId = $(this).find('option:selected').val();
                getDatasetFields(datasetId);
            });

        // place form inside container
        $container.append($legendForm);

        // preload the form with the first dataset option.
        $legendForm
            .find('#legend_' + legendNum + '_dataset option')
            .eq(1)
            .attr('selected', 'selected');

        // trigger change event
        $legendForm
            .find('#legend_' + legendNum + '_dataset')
            .change();
    };


    // by default, create a single legend creator instance.
    global.legendForms = [];
    global.legendForms.push(new LegendCreator());

    function submitForm() {
        var legends = [];
        $('#legends .legend')
            .each(function () {
                var legend = {},
                    $legend = $(this);

                legend.dataset = $legend.find('.legend-dataset option:selected').val();
                legend.name = $legend.find('.legend-name').val();
                legend.xValue = $legend.find('.legend-xValue').val();
                legend.yValue = $legend.find('.legend-yValue').val();
                legend.color = $legend.find('.legend-color').val();

                legends.push(legend);
            });

        $('#id_legends').html(JSON.stringify(legends));
        $form.submit();

    }

    $('#form-create-visualization-btn-submit').on('click', function (e) {
        e.preventDefault();
        submitForm();
    });

}(this));

