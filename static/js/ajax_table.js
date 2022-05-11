$(document).ready(function () {
  $("#ajax_data_load").click(function () {
    clicked = $(this).attr("name");
    $.ajax({
      url: "/items",
      dataSrc: "data",
      type: "POST",
      dataType: "json",
      data: $("form").serialize(),
      success: function (data) {
        console.log("Success Hit");
        console.log(data);
        location.reload();
      },
      error: function (data) {
        console.log("Error Hit");
        console.log(data);
      },
    });
  });

  $(".delete").click(function () {
    var button = $(this),
      tr = button.closest("tr");
    // find the ID stored in the .groupId cell
    var id = tr.find("td:first").text();
    console.log("clicked button with id", id);

    $.ajax({
      url: "/items/" + id,
      dataSrc: "data",
      type: "DELETE",
      dataType: "json",
      success: function (data) {
        console.log("Success Hit");
        console.log(data);
        location.reload();
      },
      error: function (data) {
        console.log("Error Hit");
        console.log(data);
      },
    });
  });
});
