<template>
  <div id="admin-main">
      <input
        v-model="task.content"
        placeholder="Enter the task"
        v-on:keyup.enter="formSubmit" />
  </div>
</template>

<script>
import { mapActions } from 'vuex';

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
    ...mapActions([
      'addTask',
    ]),
    formSubmit() {
      if (this.task.content === '') {
        return;
      }
      this.task.time = new Date();
      // const obj = Object.assign(this.task);
      this.addTask(JSON.stringify(this.task));
      this.task.content = '';
    },
  },

};
</script>

<style>

</style>
