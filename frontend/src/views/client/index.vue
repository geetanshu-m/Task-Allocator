<template>
  <div id="client-main">
    <h1>All Task</h1>
    <div id="task-list">
      <div class="task" v-for="(task, index) in allTask" :key="index">
        {{task.content}} -- {{(taskAssignTime(task.time))}}
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import moment from 'moment';

export default {
  name: 'task-list',
  computed: {
    ...mapGetters([
      'allTask',
    ]),
  },
  methods: {
    taskAssignTime(time) {
      return moment(time).calendar();
    },
  },

};
</script>

<style lang="scss">
#task-list{
  display:flex;
  flex-direction: column;
}
</style>
