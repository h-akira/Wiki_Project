document.addEventListener('DOMContentLoaded', function() {
  var toggleButton = document.getElementById('sidebar-toggle');
  var sidebar = document.getElementById('sidebar');
  toggleButton.addEventListener('click', function() {
    event.preventDefault();
    sidebar.classList.toggle('is-active');
  });
});
