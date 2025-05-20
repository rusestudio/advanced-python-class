document.addEventListener('DOMContentLoaded', () => {
    const todoList = document.getElementById('todo-list');
    const addTodoForm = document.getElementById('add-todo-form');
    const titleInput = document.getElementById('title');
    const descriptionInput = document.getElementById('description');
    const dueAtInput = document.getElementById('due_at');

    const API_BASE_URL = ''; // Keep empty if frontend/backend on same origin

    // --- Helper Functions ---
    const formatDate = (dateString) => {
        if (!dateString) return 'N/A';
        try {
            const date = new Date(dateString);
             // Adjust for timezone if needed, localeTimeString might include timezone info implicitly
             // Example: Add ' KST' if you know it's always KST, but this isn't robust
            return date.toLocaleString('ko-KR'); // Format for Korean locale
        } catch (e) {
            console.error("Error parsing date:", dateString, e);
            return 'Invalid Date';
        }
    };

    const displayError = (message) => {
        // Simple error display, could be improved (e.g., a dedicated error area)
        console.error("Error:", message);
        alert(`오류 발생: ${message}`);
    };

    // --- Render Todos ---
    const renderTodos = (todos) => {
        todoList.innerHTML = ''; // Clear existing list
        if (!todos || todos.length === 0) {
            todoList.innerHTML = '<li>등록된 할 일이 없습니다.</li>';
            return;
        }

        todos.forEach(todo => {
            const li = document.createElement('li');
            li.className = todo.completed ? 'completed' : '';
            li.dataset.id = todo.id; // Store id on the element

            // Sanitize content before inserting (basic example)
            const safeTitle = document.createTextNode(todo.title || '').textContent;
            const safeDescription = document.createTextNode(todo.description || '').textContent;

            li.innerHTML = `
                <div class="content">
                    <h3>${safeTitle}</h3>
                    <p class="description">${safeDescription || '<i>설명 없음</i>'}</p>
                    <p><small>
                        생성: ${formatDate(todo.created_at)} |
                        마감: ${formatDate(todo.due_at)}
                    </small></p>
                </div>
                <div class="actions">
                    <button class="toggle-btn">${todo.completed ? '미완료' : '완료'}</button>
                    <button class="delete-btn">삭제</button>
                </div>
            `;
            todoList.appendChild(li);
        });
    };

    // --- API Call Functions ---
    const fetchTodos = async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/todos/`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const todos = await response.json();
            renderTodos(todos);
        } catch (error) {
            displayError(`할 일 목록을 불러오지 못했습니다: ${error.message}`);
            todoList.innerHTML = '<li>목록을 불러오는데 실패했습니다.</li>';
        }
    };

    const addTodo = async (todoData) => {
         try {
            const response = await fetch(`${API_BASE_URL}/todos/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json' // Often helpful
                },
                body: JSON.stringify(todoData),
            });
            if (!response.ok) {
                 const errorData = await response.json().catch(() => ({ detail: 'Unknown error structure' })); // Try to get error detail
                 throw new Error(`HTTP error! status: ${response.status} - ${errorData.detail || response.statusText}`);
            }
            // const newTodo = await response.json(); // Get the created todo
            // Optionally add just the newTodo to the UI instead of refetching all
            fetchTodos(); // Refetch the list to include the new item
            addTodoForm.reset(); // Clear the form
        } catch (error) {
             displayError(`할 일을 추가하지 못했습니다: ${error.message}`);
        }
    };

    const toggleComplete = async (id) => {
        try {
            const response = await fetch(`${API_BASE_URL}/todos/${id}/toggle`, {
                method: 'PATCH',
                headers: { 'Accept': 'application/json' }
            });
             if (!response.ok) {
                 const errorData = await response.json().catch(() => ({ detail: 'Unknown error structure' }));
                 throw new Error(`HTTP error! status: ${response.status} - ${errorData.detail || response.statusText}`);
            }
            // const updatedTodo = await response.json();
            // Optionally update just this item in the UI instead of refetching
             fetchTodos(); // Refetch to update UI
        } catch (error) {
            displayError(`상태 변경에 실패했습니다: ${error.message}`);
        }
    };

    const deleteTodo = async (id) => {
         try {
            const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
                method: 'DELETE',
            });
             if (!response.ok && response.status !== 204) { // 204 No Content is success for DELETE
                 const errorData = await response.json().catch(() => ({ detail: 'Unknown error structure' }));
                 throw new Error(`HTTP error! status: ${response.status} - ${errorData.detail || response.statusText}`);
            }
            // Optionally remove the item directly from the UI instead of refetching
             fetchTodos(); // Refetch to update UI
        } catch (error) {
            displayError(`삭제에 실패했습니다: ${error.message}`);
        }
    };


    // --- Event Listeners ---
    addTodoForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default page reload

        const newTodoData = {
            title: titleInput.value.trim(),
            description: descriptionInput.value.trim(),
            // Get value and ensure it's null if empty, otherwise format for Pydantic
            due_at: dueAtInput.value ? new Date(dueAtInput.value).toISOString() : null,
            completed: false // New todos are incomplete by default
        };

        if (!newTodoData.title) {
            alert("제목을 입력해주세요.");
            return;
        }

        addTodo(newTodoData);
    });

    // Event delegation for toggle and delete buttons
    todoList.addEventListener('click', (event) => {
        const target = event.target;
        const listItem = target.closest('li'); // Find the parent li element

        if (!listItem) return; // Click wasn't inside a list item

        const todoId = listItem.dataset.id;

        if (target.classList.contains('toggle-btn')) {
            toggleComplete(todoId);
        } else if (target.classList.contains('delete-btn')) {
            if (confirm('정말로 이 항목을 삭제하시겠습니까?')) {
                deleteTodo(todoId);
            }
        }
    });

    // --- Initial Load ---
    fetchTodos();

});