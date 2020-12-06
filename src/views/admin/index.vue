<template>
  <div id="admin-main">
      <input
        v-model="task.content"
        placeholder="Enter the task"
        v-on:keyup.enter="formSubmit" />
  </div>
</template>

<script>
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
      console.log(JSON.stringify(this.task));
      this.task.content = '';
    },
  },

};
</script>

<style>

</style>
