/*jslint devel: true, browser: true, nomen: true, maxerr: 50, indent: 4 */
/*global jQuery, $, _*/

(function (global) {
    "use strict";

    var schema,
        template = _.template($('#add-more-fields-template').html()),
        fieldCount = 0;

    /**
     * gets all the schema field values and returns them as an object.
     */
    function getFields() {
        var data = {};
        $('#form-create-datatype .fields .field').each(function () {
            var $this = $(this),
                fieldName = $this.find('input.field-name').val(),
                fieldType = $this.find('select.field-type option:selected').val();
            data[fieldName] = fieldType;
        });

        return data;
    }


    function updateJSONPreview() {
        var preview = {
            type: $('#form-create-datatype #id_name').val(),
            data: getFields()
        };

        $('#create-datatype-json-schema').text(JSON.stringify(preview, undefined, 4));
    }


    /**
     * Updates the JSON preview every time an input field is changed.
     * @return {undefined}
     */
    function bindChangeEvents() {
        $('#form-create-datatype input, #form-create-datatype select').off('change');
        $('#form-create-datatype input, #form-create-datatype select').on('change', function () {
            updateJSONPreview();
        });
    }


    /**
     * Appends another datatype field to the form.
     */
    function addDataTypeField() {
        $('#form-create-datatype .fields').append(template({fieldNum: fieldCount}));
        fieldCount += 1;
        bindChangeEvents();
    }


    $('#form-create-datatype-btn-add-more-fields').click(function (e) {
        e.preventDefault();
        addDataTypeField();
    });

    $('#form-create-datatype-btn-submit').click(function (e) {
        e.preventDefault();

        $('#id_schema').text(JSON.stringify(getFields()));
        $('#form-create-datatype').submit();
    });

    addDataTypeField();

}(this));