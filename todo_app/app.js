document.addEventListener("DOMContentLoaded", function () {
  const taskInput = document.getElementById("taskInput");
  const addTaskBtn = document.getElementById("addTaskBtn");
  const taskList = document.getElementById("taskList");
  addTaskBtn.addEventListener("click", function () {
    const taskText = taskInput.value.trim();
    if (taskText) {
      const taskItem = document.createElement("li");
      taskItem.innerHTML = `${taskText} <button>Edit</button> <button>Delete</button>`;
      taskItem.querySelector("button").addEventListener("click", function () {
        const newTaskText = prompt("Edit your task", taskText);
        if (newTaskText) {
          taskItem.firstChild.textContent = newTaskText + " ";
        }
      });
      taskItem
        .querySelectorAll("button")[1]
        .addEventListener("click", function () {
          taskList.removeChild(taskItem);
        });
      taskList.appendChild(taskItem);
      taskInput.value = "";
    }
  });
});
