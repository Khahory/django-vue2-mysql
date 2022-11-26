<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <section>
            <b-button>Click Me</b-button>
        </section>
        <HelloWorld msg="Welcome to Your Vue.js App"/>
    </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: 'HomeView',
    components: {
        HelloWorld
    }
}
</script>
