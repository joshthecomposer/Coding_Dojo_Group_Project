$(document).ready(function() {
    $('.edit-form').on('submit', function (e) {
        e.preventDefault();
        data = $('.edit-form').serialize()
        console.log()
        $.ajax({
            method: 'POST',
            url: "/edit_timer",
            data: data,
            cache: false,
            success: function (data) {
                e = document.getElementById(`timer-${data.id}-container`)
                e.children[0].innerText = "Name: "+data.name
                e.children[1].innerText = "Exercise (seconds): "+data.exercise_time
                e.children[2].innerText = "Rest (seconds): "+data.rest_time
                e.children[3].innerText = "Total Sets: " + data.sets
                hideEdit()
                return false;
            }
        })
    });
});



let blurElement = document.getElementById('blur');
let edit;







function revealEdit(id, name) {
    edit = document.getElementById(`${id} ${name}`);
    $(blurElement).addClass("disabled-btn");
    filterVal = "blur(50px)"
    $(edit).fadeIn(500)
    $(blurElement).css({
        'filter':filterVal,
        'webkitFilter':filterVal,
        'mozFilter':filterVal,
        'oFilter':filterVal,
        'msFilter': filterVal,
        'transition':'all 0.5s ease-in',
        '-webkit-transition':'all 0.5s ease-in',
        '-moz-transition':'all 0.5s ease-in',
        '-o-transition':'all 0.5s ease-in'
    });
};

function hideEdit() {
    filterVal = "blur(0)"
    $(edit).fadeOut(500)
    $(blurElement).css({
        'filter':filterVal,
        'webkitFilter':filterVal,
        'mozFilter':filterVal,
        'oFilter':filterVal,
        'msFilter':filterVal,
        'transition':'all 0.5s ease-in',
        '-webkit-transition':'all 0.5s ease-in',
        '-moz-transition':'all 0.5s ease-in',
        '-o-transition':'all 0.5s ease-in'
    });
    $(blurElement).removeClass("disabled-btn");
};