$(function () {
  $.get('https://swapi.co/api/films/?format=json', (data, status) => {
    if (status === 'success') {
      for (let movie of data.results) {
        $('ul#list_movies').append($('<li></li>').text(movie['title']));
      }
    }
  });
});
