<template>
  <div class="container">
    <!-- Heading -->
    <h2 class="text-center mt-5">My Vue Todo App</h2>
    <div class="d-flex ml-auto mt-5">
      <button type="button" class="btn btn-outline-success ml-auto" data-toggle="modal"
              data-target="#exampleModalCenter">
        ToDo Olustur
      </button>
    </div>
    <div class="input-group col-8 mt-2">
      <input v-model="keyword" type="text" class="form-control" placeholder="Search by Group or Priority or Due Date">
    </div>
    <div class="modal fade bd-example-modal-xl" id="exampleModalCenter" tabindex="-1" role="dialog"
         aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-xl" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div>
              <div class="col-6">
                <label>Groups</label>
                <multiselect
                    v-model="task.groups"
                    tag-placeholder="Not Found!"
                    placeholder="Group Title"
                    label="title"
                    track-by="id"
                    :options="options"
                    :multiple="false"
                    :taggable="false"
                />
              </div>
              <div class="d-flex mt-2" style="align-items: end;">
                <div class="col-2">
                  <input
                      type="text"
                      v-model="task.title"
                      placeholder="Enter task"
                      class="w-100 form-control mr-2"
                  />
                </div>
                <div class="col-2">
                  <label>Is Active</label>
                  <div class="custom-control custom-switch">
                    <input
                        id="customSwitch3"
                        v-model="task.isActive"
                        type="checkbox"
                        class="custom-control-input"
                        required
                    >
                    <label class="custom-control-label" for="customSwitch3">Is Active</label>
                  </div>
                </div>
                <div class="col-2">
                  <label>Completed</label>
                  <div class="custom-control custom-switch">
                    <input
                        id="customSwitch2"
                        v-model="task.completed"
                        type="checkbox"
                        class="custom-control-input"
                        required
                    >
                    <label class="custom-control-label" for="customSwitch2">Completed</label>
                  </div>
                </div>
                <div class="form-group col-3 m-0">
                  <label for="exampleFormControlSelect1">Priority</label>
                  <select class="form-control" id="exampleFormControlSelect1" v-model="task.priority">
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                    <option>5</option>
                  </select>
                </div>
                <div class="col-3">
                  <input
                      type="date"
                      v-model="task.due_date"
                      placeholder="Enter task"
                      class="w-100 form-control mr-2"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button v-if="!popUp" type="button" class="btn btn-secondary" data-dismiss="modal" @click="clearToDO">
              Close
            </button>
            <button v-if="popUp" type="button" class="btn btn-secondary" data-dismiss="modal" @click="deleteToDo(task)">
              Delete
            </button>
            <button v-if="!popUp" type="button" class="btn btn-primary" @click="saveToDO">Save changes</button>
            <button v-if="popUp" type="button" class="btn btn-primary" @click="updateToDo(task)">Update</button>
          </div>
        </div>
      </div>
    </div>


    <!-- Task table -->
    <table class="table table-bordered mt-5">
      <thead>
      <tr>
        <th scope="col" class="text-center">ToDo Title</th>
        <th scope="col" class="text-center">Group Name</th>
        <th scope="col" style="width: 120px">IsActive</th>
        <th scope="col" style="width: 120px">Completed</th>
        <th scope="col" style="width: 120px">Priority</th>
        <th scope="col" class="text-center">Due Date</th>
        <th scope="col" class="text-center">Operation</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(task, index) in todoList" :key="index">
        <td>
          {{ task.title }}
        </td>
        <td>
          {{ task.groups.title }}
        </td>
        <td>
          {{ task.is_active ? 'Devam Ediyor' : 'Pasif' }}
        </td>
        <td>
            <span :class="{ 'line-through': task.completed === true }">
               {{ task.completed ? 'Tamamlandı' : 'Devam Ediyor' }}
            </span>
        </td>
        <td>
          {{ task.priority }}
        </td>
        <td class="text-center">
          {{ task.due_date }}
        </td>
        <td>
          <div class="d-flex">
            <button class="btn btn-outline-info mr-1" @click="update(task)">
              Operations
            </button>
          </div>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

import Multiselect from 'vue-multiselect'
import axios from "axios";
import Vue from "vue";

export default {
  name: "ToDo",
  components: {Multiselect},
  data() {
    return {
      task: {
        title: '',
        isActive: true,
        completed: false,
        priority: 1,
        due_date: null,
        groups: -1,
      },
      keyword: '',
      editedTask: null,
      options: [],
      value: '',
      todoList: [],
      popUp: false,
    };
  },
  watch: {
    keyword(newKeyword, oldKeyword) {
      if (newKeyword !== oldKeyword) {
        this.getAllTodos(newKeyword)
      }
    }
  },
  created() {
    this.getAllGroups()
    this.getAllTodos()
  },
  methods: {
    getAllGroups() {
      axios.get('todos/groups/').then(r => {
        this.options = r.data.results
      })
    },
    getAllTodos(search_query = '') {
      if (search_query === '') {
        axios.get('todos/todo/').then(r => {
        this.todoList = r.data.results
       })
      } else {
        axios.get(`todos/todo/?search=${search_query}`).then((r) => {
                this.todoList = r.data.results
            })
      }

    },
    capitalizeFirstChar(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    },
    update(v) {
      $('#exampleModalCenter').modal('toggle')
      this.task = {...v}
      this.popUp = true
    },
    updateToDo(s) {
      this.task.groups = this.task.groups.id
      axios.put(`todos/todo/${s.id}/`, this.task).then(r => {
        this.getAllTodos()
        Vue.notify({
          type: 'success',
          title: 'Başarılı',
          text: 'Başarıyla güncellediniz!',
        });
      })
      $('#exampleModalCenter').modal('hide')
    },
    deleteToDo(s) {
      this.task.groups = this.task.groups.id
      axios.delete(`todos/todo/${s.id}/`).then(r => {
        Vue.notify({
          type: 'success',
          title: 'Başarılı',
          text: 'Başarıyla sildiniz!',
        });
      })
      this.getAllTodos()
    },
    saveToDO() {
      this.task.groups = this.task.groups.id
      axios.post('todos/todo/', this.task).then(r => {
        this.getAllTodos()
        Vue.notify({
          type: 'success',
          title: 'Başarılı',
          text: 'Başarıyla todo oluşturdunuz!',
        });
      })
      this.clearToDO()
    },
    clearToDO() {
      this.task = {
        title: '',
        isActive: true,
        completed: false,
        priority: 1,
        due_date: null,
        groups: -1,
      }
    }
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>


<style scoped>
.pointer {
  cursor: pointer;
}

.line-through {
  text-decoration: line-through;
}
</style>