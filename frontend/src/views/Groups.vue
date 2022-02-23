<template>
  <div class="container" style="max-width: 600px">
    <div class="d-flex mt-5">
      <input
        type="text"
        v-model="title"
        placeholder="Group Title"
        class="w-100 form-control"
      />
      <button class="btn btn-warning rounded-0 ml-2" @click="submitTask">
        SUBMIT
      </button>
    </div>
    <table class="table table-bordered mt-5">
      <thead>
        <tr>
          <th scope="col">Group</th>
          <th scope="col" style="width: 120px">Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(m, index) in groups" :key="index">
          <td>
              {{ capitalizeFirstChar(m.title) }}
          </td>
          <td>
            <div class="d-flex">
              <button class="btn btn-outline-info mr-1" @click="updatePopUp(m)">
                    Update
                </button>
               <button class="btn btn-outline-danger" @click="deleteGroup(m)">
                    Delete
                </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
     <div v-if="update" class="d-flex mt-5">
      <input
        type="text"
        v-model="group.title"
        placeholder="Group Title"
        class="w-100 form-control"
      />
      <button class="btn btn-warning rounded-0 ml-2" @click="updateValue">
        Update
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Vue from "vue";

export default {
  name: "Groups",
  data() {
    return {
      title: "",
      value: "",
      groups: [],
      update: false,
      group: {
        'id': null,
        'title': null,
      }
    };
  },
  created() {
    this.getAllGroups()
    console.log(this.groups)
  },
  methods: {
    capitalizeFirstChar(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    },
    submitTask() {
      if (this.title === 0) return;
      axios.post('todos/groups/', {'title': this.title}).then(r=> {
        Vue.notify({
                type: 'success',
                title: 'Başarılı',
                text: 'Başarıyla grup oluşturdunuz!',
              });
      })
      this.getAllGroups()
    },
    getAllGroups() {
      axios.get('todos/groups/').then( r => {
        this.groups = r.data.results
      })
    },
    updatePopUp (group) {
      this.group = {...group}
      this.update = true
    },
    updateValue () {
      axios.put(`todos/groups/${this.group.id}/`,{'title': this.group.title}).then(r=> {
        Vue.notify({
                type: 'success',
                title: 'Başarılı',
                text: 'Başarıyla güncellediniz!',
              });
        this.getAllGroups()
      })
    },
    deleteGroup(group) {
      axios.delete(`todos/groups/${group.id}/`).then(r=> {
        Vue.notify({
                type: 'success',
                title: 'Başarılı',
                text: 'Başarıyla sildiniz!',
              });
        this.getAllGroups()
      })
    }
  },
};
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Edge, Opera and Firefox */
}
.line-through {
  text-decoration: line-through;
}
</style>