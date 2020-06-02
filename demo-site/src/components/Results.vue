<template>
    <div class="results row col-12">
        <Result v-for="(result, index) in results" v-bind:key="index" v-bind:result="result">
        </Result>
    </div>
</template>

<script>
    import Result from "./Result";

    export default {
        name: "Results",
        components: {Result},
        props: ['results']
    }
</script>

<style scoped>
    .results {
        color: #333;
        margin-top: 40px;
        overflow-y: scroll;
        max-height: 450px;
        margin-left: 0;
        padding: 0;
        border-radius: .25rem;
        font-size: 18px !important;
        margin-bottom: 100px;
        background: linear-gradient(white, white, #efefef);
    }
</style>