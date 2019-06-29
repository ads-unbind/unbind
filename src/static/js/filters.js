/* Table filters */

(function() {
    'use strict';
    var $ = jQuery;
    $.fn.extend({
        filterTable: function() {
            return this.each(function() {
                $(this).on('keyup', function(e) {
                    $('.filterTable_no_results').remove();
                    var $this = $(this),
                        search = $this.val().toLowerCase(),
                        target = $this.attr('data-filters'),
                        $target = $(target),
                        $rows = $target.find('tbody tr');

                    if (search == '') {
                        $rows.show();
                    } else {
                        $rows.each(function() {
                            var $this = $(this);
                            $this.text().toLowerCase().indexOf(search) === -1 ? $this.hide() : $this.show();
                        })
                        if ($target.find('tbody tr:visible').size() === 0) {
                            var col_count = $target.find('tr').first().find('td').size();
                            var no_results = $('<tr class="filterTable_no_results"><td colspan="' + col_count + '">Categoria não encontrada</td></tr>')
                            $target.find('tbody').append(no_results);
                        }
                    }
                });
            });
        }
    });
    $('[data-action="filter"]').filterTable();
})(jQuery);

$(function() {
    // attach table filter plugin to inputs
    $('[data-action="filter"]').filterTable();

    $('.container').on('click', '.panel-heading span.filter', function(e) {
        var $this = $(this),
            $panel = $this.parents('.panel');

        $panel.find('.panel-body').slideToggle();
        if ($this.css('display') != 'none') {
            $panel.find('.panel-body input').focus();
        }
    });
    $('[data-toggle="tooltip"]').tooltip();
})

/* Card Filter */

// search function
$(document).ready(function() {
    $("#cardFilter").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#filtered .card").hide().closest('#cardItem').hide(); // hide all cards and its closest rows
        $("#filtered .card").filter(function() {
            return $(this).text().toLowerCase().indexOf(value) > -1; // return true or false from filter
        }).show().closest('#cardItem').show(); // then show the card and its closest row after filter
    });
});