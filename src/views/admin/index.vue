<template>
  <div id="admin-main">
      <input
        v-model="task.content"
        placeholder="Enter the task"
        v-on:keyup.enter="formSubmit" />
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'admin-screen',
  data() {
    return {
      task: {
        content: '',
        time: '',
      },
    };
  },
  methods: {
    formSubmit() {
      if (this.task.content === '') {
        return;
      }
      this.task.time = new Date();
      // const obj = Object.assign(this.task);
      // this.sendTask(JSON.stringify(this.task));
      axios.post(
        'http://localhost:3000/addTask',
        this.task,
      ).then((res) => {
        console.log('success send', res);
      })
        .catch((err) => {
          console.log('some error occured', err);
        });
      this.task.content = '';
    },
  },

};
</script>

<style>

</style>
