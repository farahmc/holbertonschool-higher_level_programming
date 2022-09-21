// script that adds, removes and clears LI elements from a list when the user clicks
// When the user clicks on DIV#add_item: a new element is added to the list
// When the user clicks on DIV#remove_item: the last element is removed from the list
// When the user clicks on DIV#clear_list: all elements of the list are removed

document.addEventListener('DOMContentLoaded', () => {
    $('#add_item').click(function () {
        $('UL.my_list').append('<li>Item</li>')
    });
    $('#remove_item').click(function () {
        $('UL.my_list li:last-child').remove()
    });
    $('#clear_list').click(function () {
        $('UL.my_list').empty()
    });
    }
);