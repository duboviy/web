function editBook(id, name, authors){
    $('.changeable').attr('action', '/edit-book/' + id);
    $('.edit-form > #name').val(name);
    $('.edit-form > #authors').val(authors);
    return false;
}

function editAuthor(id, name, books){
    $('.changeable').attr('action', '/edit-author/' + id);
    $('.edit-form > #name').val(name);
    $('.edit-form > #books').val(books);
    return false;
}