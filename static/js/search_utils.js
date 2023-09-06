// Функция, которая устанавливает значения дат в зависимости от выбранного периода
function setDates() {
    // Получаем элемент select по id
    var period = document.getElementById("id_date_period");

    // Создаем объект даты для текущего дня
    var today = new Date();
    var start, end;
    // Получаем значение выбранного option
    var select = period.value;
    if (select == 0){ // today
        start = today;
        end = today;
    }
    if (select == 1){ // last week
        start = new Date(today.getTime() - 7 * 24 * 60 * 60 * 1000);
        end = today;
    }
    if (select == 2){ // current month
        start = new Date(today.getFullYear(), today.getMonth(), 2);
        end = new Date(today.getFullYear(), today.getMonth() + 1, 1);
    }
    if (select == 3){ //current year
        start = new Date(today.getFullYear(), 0, 2);
        end = new Date(today.getFullYear(), 12, 1);
    }

    var startStr = start.toISOString().slice(0,10);
    var endStr = end.toISOString().slice(0,10);
    // Получаем элементы input type="date" по id
    var startDate = document.getElementById("id_date_start");
    var endDate = document.getElementById("id_date_end");
    // Устанавливаем значения input type="date" равными отформатированным датам
    startDate.value = startStr;
    endDate.value = endStr;
}

function showHidePanel() {
    // Получаем элемент select по id
    var period = document.getElementById("id_date_period");
}