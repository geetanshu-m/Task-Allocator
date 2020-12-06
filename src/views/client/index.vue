<template>
  <div id="client-main">
    <h1>All Task</h1>
    <div id="task-list">
      <div class="task" v-for="(task, index) in allTask" :key="index">
        {{task}}
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'task-list',
  computed: {
    ...mapGetters([
      'allTask',
    ]),
  },

};
</script>

<style lang="scss">
#task-list{
  display:flex;
  flex-direction: column;
}
</style>
