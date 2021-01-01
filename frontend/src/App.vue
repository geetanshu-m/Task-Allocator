<template>
  <div id="app">
    <header/>
    <main-container/>
  </div>
</template>
<script>
import header from '@/components/layout/header.vue'
import mainContainer from '@/components/layout/mainContainer.vue'

export default {
  name: 'main-app',
  components:{
    header,
    mainContainer
  }
};
</script>

<style lang="scss">
body{
  padding:0px;
  margin:0px;
}
</style>
