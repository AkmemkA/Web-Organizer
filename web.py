import streamlit as st
import functions


todos = functions.get_todos("/Users/kodi1993/PycharmProjects/pythonProject/todos.txt")


def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos, "/Users/kodi1993/PycharmProjects/pythonProject/todos.txt")


st.title("My ToDo App")
st.subheader("List Of Todos")

for index, i in enumerate(todos):
    checkbox = st.checkbox(i.capitalize(), key=i)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, "/Users/kodi1993/PycharmProjects/pythonProject/todos.txt")
        del st.session_state[i]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter ToDo:",
              on_change=add_todo, key='new todo')

st.session_state



