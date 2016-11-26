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
    $.snackbar({
      content: 'UPVOTE!',
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
  })

  jQuery('.btn-comment').on('click', function(e) {
    var $this = $(this)

    updateBadge(this, 0)

    jQuery.ajax({
      method: 'POST',
      url: '/add_reaction'
    })

    $this
      .data('commented', true)
      .off('click')
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

    $('#js-comment-form').slideDown()
  })
  .on('mouseenter', function(e) {
    updateBadge(this, 1)
  })
  .on('mouseleave', function(e) {
    updateBadge(this, -1)
  })

})()
