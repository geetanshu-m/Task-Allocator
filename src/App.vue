<template>
  <div id="app">
    <div id="nav">
      <router-link to="/client">Client View</router-link> |
      <router-link to="/admin">Admin View</router-link>
    </div>
    <router-view/>
  </div>
</template>
<script>
import io from 'socket.io-client';
import { mapActions } from 'vuex';

export default {
  name: 'main-app',
  methods: {
    ...mapActions([
      'addTask',
    ]),
  },
  mounted() {
    const socket = io('http://localhost:3000');
    // const socket = new WebSocket('ws://localhost:3000');

    socket.on('message', (evt) => {
      this.addTask(evt);
    });
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
