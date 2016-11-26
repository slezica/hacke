(function() {
  var updateBadge = function(el, multiplier) {
    var $el = $(el)
    if ($el.data('commented')) return

    multiplier = multiplier == null ? 1 : multiplier

    $el.find('.badge').text(function(index, old) {
      return parseInt(old) + (1 * multiplier)
    })
  }

  jQuery('.upvote-icon').on('click', function() {
    var icons = $(this).closest('.icons')

    if (icons.hasClass('voted')) return

    $.snackbar({
      content: 'Comentario votado!',
      style: 'toast',
      timeout: 1000
    })

    var form = $(this).closest('form')[0]
    var formData = new FormData(form)

    jQuery.ajax({
      method: 'POST',
      url: form.action,
      data: formData,
      processData: false,
      contentType: false
    })

    debugger

    icons
      .addClass('voted')
      .find('.js-votes-count')
      .text(function(index, old) {
        return parseInt(old) + 1
      })
  })

  jQuery('.btn-comment').on('click', function(e) {
    var $this = $(this)
    var form = $this.closest('form')[0]
    var type = $this.data('type')

    updateBadge(this, 0)

    jQuery('.js-hidden-type').val(type)

    jQuery.ajax({
      method: 'POST',
      url: form.action,
      data: new FormData(form),
      processData: false,
      contentType: false,
      success: function(response) {
        debugger
        jQuery('.js-hidden-reaction').val(response)
      }
    })

    $this
      .data('commented', true)
      .off()
      .addClass('selected')

    if (jQuery("#js-mobile-check").css('display') === 'none') {
      $this
        .animate({ width: '100%' }, 500)

      $this
        .siblings('.btn')
        .addClass('hidden')

    } else {
      $this
        .animate({ width: '100%' }, 500)
        .addClass('selected')

      $this
        .siblings('.btn')
        .animate({ width: 0, paddingRight: 0, paddingLeft: 0 }, 400)
    }

    jQuery('#js-comment-form')
      .slideDown()
  })
  .on('mouseenter', ':not(.selected)', function(e) {
    updateBadge(this, 1)
  })
  .on('mouseleave', ':not(.selected)', function(e) {
    updateBadge(this, -1)
  })

})()
