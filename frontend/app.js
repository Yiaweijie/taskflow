/**
 * TaskFlow - Frontend Application
 * Handles rendering tasks and communicating with the API.
 */

const API_URL = "http://localhost:5000/api";

// Fetch and render all tasks
async function loadTasks() {
    try {
        const response = await fetch(`${API_URL}/tasks`);
        const tasks = await response.json();
        renderTasks(tasks);
    } catch (error) {
        console.error("Failed to load tasks:", error);
        // Fallback: load from local tasks.json if API is down
        loadLocalTasks();
    }
}

// Fallback for when API isn't running
async function loadLocalTasks() {
    try {
        const response = await fetch("../backend/tasks.json");
        const tasks = await response.json();
        renderTasks(tasks);
    } catch (error) {
        console.error("No tasks available");
    }
}

// Render tasks into the kanban columns
function renderTasks(tasks) {
    const todoList = document.getElementById("todo-list");
    const progressList = document.getElementById("progress-list");
    const doneList = document.getElementById("done-list");

    // Clear existing
    todoList.innerHTML = "";
    progressList.innerHTML = "";
    doneList.innerHTML = "";

    tasks.forEach(task => {
        const card = createTaskCard(task);

        switch (task.status) {
            case "todo":
                todoList.appendChild(card);
                break;
            case "in_progress":
                progressList.appendChild(card);
                break;
            case "done":
                doneList.appendChild(card);
                break;
        }
    });
}

// Create a task card element
function createTaskCard(task) {
    const card = document.createElement("div");
    card.className = `task-card priority-${task.priority}`;
    card.dataset.id = task.id;

    card.innerHTML = `
        <h4>${task.title}</h4>
        <p>${task.description}</p>
        ${task.assignee ? `<div class="assignee">Assigned to: ${task.assignee}</div>` : ""}
    `;

    card.addEventListener("click", () => cycleStatus(task.id, task.status));
    return card;
}

// Cycle task status on click: todo -> in_progress -> done -> todo
async function cycleStatus(taskId, currentStatus) {
    const statusOrder = ["todo", "in_progress", "done"];
    const currentIndex = statusOrder.indexOf(currentStatus);
    const nextStatus = statusOrder[(currentIndex + 1) % statusOrder.length];

    try {
        await fetch(`${API_URL}/tasks/${taskId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ status: nextStatus }),
        });
        loadTasks();
    } catch (error) {
        console.error("Failed to update task:", error);
    }
}

// Handle new task form submission
document.getElementById("task-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const title = document.getElementById("task-title").value;
    const description = document.getElementById("task-desc").value;
    const priority = document.getElementById("task-priority").value;

    try {
        await fetch(`${API_URL}/tasks`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, description, priority }),
        });

        // Clear form
        document.getElementById("task-title").value = "";
        document.getElementById("task-desc").value = "";
        document.getElementById("task-priority").value = "medium";

        loadTasks();
    } catch (error) {
        console.error("Failed to create task:", error);
    }
});

// Load tasks on page load
document.addEventListener("DOMContentLoaded", loadTasks);
