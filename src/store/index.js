import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    taskList: [],
  },
  mutations: {
    ADD_TASK(state, task) {
      state.taskList.push(task);
    },
  },
  actions: {
    addTask({ commit }, task) {
      commit('ADD_TASK', task);
    },
  },
  getters: {
    allTask(state) {
      return state.taskList;
    },
  },
  modules: {
  },
});
