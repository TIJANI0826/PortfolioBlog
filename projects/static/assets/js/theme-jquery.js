/**
 * @author uiocean
 * @version 1.0
 *
 */
(function($) {
    "use strict";
    var EL = {};
    $.fn.exists = function() {
        return this.length > 0;
    };


    /* ---------------------------------------------- /*
     * Header height
    /* ---------------------------------------------- */
    EL.HeaderHeight = function() {
        var HHeight = $('.header-height').outerHeight()
        var HHeightTop = $('.header-top').outerHeight()
        $('.header-height-bar').css("min-height", HHeight);
    }


    // Window on Load
    $(window).on("load", function() {
    });
    // Document on Ready
    $(document).ready(function() {
        EL.HeaderHeight();
    });

    // Document on Scrool
    $(window).scroll(function() {
    });

    // Window on Resize
    $(window).resize(function() {
        EL.HeaderHeight();
    });

})(jQuery);