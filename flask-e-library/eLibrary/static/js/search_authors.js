var mas;
var table = $('#author-list');
var switchSearch = 'Books';

function generateTableRow(author){
    var result = '<tr><td>'+ author.name +'</td><td>' + author.books + '</td>'
    if($('#addModal').length)
        result += '<td> <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#editModal" onclick="editAuthor(' + author.id + ', \'' + author.name + '\', \'' + author.books + '\')"><span class="glyphicon glyphicon-pencil"></span></button> &nbsp;<a href="/remove-author/' + author.id + '"><span class="glyphicon glyphicon-remove"></span></a></td></tr>'

    return result
}

$( document ).ready(function() {
    $.ajax({
        type: 'POST',
        url: '/get-author-list',
        success: function(authors){

            mas = JSON.parse(authors);
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

    $('#author-list').find("tr:gt(0)").remove();

    for (var i = 0; i < mas.length; i++) {
        if(!search.trim()){
            table.append(generateTableRow(mas[i]));
        }
        else if(switchSearch=='Authors') {
            if (mas[i].name.toUpperCase().indexOf(search.toUpperCase()) > -1) {
                table.append(generateTableRow(mas[i]));
            }
        }
        else if(switchSearch=='Books') {
            for(var j = 0; j < mas[i].books.length; j++)
                if (mas[i].books[j].toUpperCase().indexOf(search.toUpperCase()) > -1) {
                    table.append(generateTableRow(mas[i]));
                }
        }
    }
});