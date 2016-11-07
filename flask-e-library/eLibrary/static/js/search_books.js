var mas;
var table = $('#book-list');
var switchSearch = 'Books';

function generateTableRow(book){
    var result = '<tr><td>'+ book.name +'</td><td>' + book.authors + '</td>'
    if($('#addModal').length)
        result += '<td> <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#editModal" onclick="editBook(' + book.id + ', \'' + book.name + '\', \'' + book.authors + '\')"><span class="glyphicon glyphicon-pencil"></span></button> &nbsp;<a href="/remove-book/' + book.id + '"><span class="glyphicon glyphicon-remove"></span></a></td></tr>'

    return result
}

$( document ).ready(function() {
    $.ajax({
        type: 'POST',
        url: '/get-book-list',
        success: function(books){

            mas = JSON.parse(books);
            for(var i = 0; i < mas.length; i++){
                table.append(generateTableRow(mas[i]));
            }
        }
    })
});

$('.dropdown-menu a').click(function(){
    $('#switchSearch').text($(this).text());
    switchSearch = $(this).text();
});

$ ('#search-button').click(function() {
    var search = $('#search-input').val();

    $('#book-list').find("tr:gt(0)").remove();

    for (var i = 0; i < mas.length; i++) {
        if(!search.trim()){
            table.append(generateTableRow(mas[i]));
        }
        else if(switchSearch=='Books') {
            if (mas[i].name.toUpperCase().indexOf(search.toUpperCase()) > -1) {
                table.append(generateTableRow(mas[i]));
            }
        }
        else if(switchSearch=='Authors') {
            for(var j = 0; j < mas[i].authors.length; j++)
                if (mas[i].authors[j].toUpperCase().indexOf(search.toUpperCase()) > -1) {
                    table.append(generateTableRow(mas[i]));
                }
        }
    }
});