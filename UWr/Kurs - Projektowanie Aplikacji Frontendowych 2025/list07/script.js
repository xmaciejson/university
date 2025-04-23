document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("add-todo-form");
    const input = form.querySelector("input[name='todo-name']");
    const list = document.getElementById("todo-list");
    const countSpan = document.getElementById("count");
    const clearButton = document.getElementById("todos-clear");
  
    const updateCount = () => {
      const remaining = list.querySelectorAll(
        ".todo__container:not(.todo__container--completed)"
      );
      countSpan.textContent = remaining.length;
    };
  
    const createTodoElement = (text, isCompleted = false) => {
      const li = document.createElement("li");
      li.classList.add("todo__container");
      if (isCompleted) li.classList.add("todo__container--completed");
  
      const nameDiv = document.createElement("div");
      nameDiv.classList.add("todo-element", "todo-name");
      nameDiv.textContent = text;
  
      const upBtn = document.createElement("button");
      upBtn.classList.add("todo-element", "todo-button", "move-up");
      upBtn.textContent = "↑";
  
      const downBtn = document.createElement("button");
      downBtn.classList.add("todo-element", "todo-button", "move-down");
      downBtn.textContent = "↓";
  
      const statusBtn = document.createElement("button");
      statusBtn.classList.add("todo-element", "todo-button");
      statusBtn.textContent = isCompleted ? "Revert" : "Done";
  
      const removeBtn = document.createElement("button");
      removeBtn.classList.add("todo-element", "todo-button");
      removeBtn.textContent = "Remove";
  
      li.append(nameDiv, upBtn, downBtn, statusBtn, removeBtn);
      return li;
    };
  
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const text = input.value.trim();
      if (!text) return;
      const newTodo = createTodoElement(text);
      list.appendChild(newTodo);
      input.value = "";
      updateCount();
    });
  
    list.addEventListener("click", (e) => {
      if (!e.target.classList.contains("todo-button")) return;
  
      const li = e.target.closest(".todo__container");
  
      if (e.target.textContent === "Done") {
        const updated = createTodoElement(
          li.querySelector(".todo-name").textContent,
          true
        );
        list.replaceChild(updated, li);
      }
  
      if (e.target.textContent === "Revert") {
        const updated = createTodoElement(
          li.querySelector(".todo-name").textContent,
          false
        );
        list.replaceChild(updated, li);
      }
  
      if (e.target.textContent === "Remove") {
        li.remove();
      }
  
      if (e.target.classList.contains("move-up")) {
        const prev = li.previousElementSibling;
        if (prev) list.insertBefore(li, prev);
      }
  
      if (e.target.classList.contains("move-down")) {
        const next = li.nextElementSibling;
        if (next) list.insertBefore(next, li);
      }
  
      updateCount();
    });
  
    clearButton.addEventListener("click", () => {
      list.innerHTML = "";
      updateCount();
    });
  });
  