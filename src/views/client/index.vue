<template>
  <div id="client-main">
    <h1>All Task</h1>
    <div id="task-list">
      <div class="task" v-for="(task, index) in taskList" :key="index">
        {{task.content}}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'task-list',
  data() {
    return {
      taskList: [
        {
          content: 'task 1',
        },
        {
          content: 'task 2',
        },
        {
          content: 'task 3',
        },
        {
          content: 'task 4',
        },
      ],
    };
  },

};
</script>

<style lang="scss">
#task-list{
  display:flex;
  flex-direction: column;
}
</style>
