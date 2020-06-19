<template>
    <b-container id="app" class="container">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="author" content="allerria">
        <meta name="description" content="sakha-ner">
        <title>Sakha NER</title>
        <Title></Title>
        <Description></Description>
        <Main></Main>
    </b-container>
</template>

<script>
    import Title from './components/Title'
    import Main from './components/Main'
    import Description from './components/Description'

    export default {
        name: 'App',
        components: {
            Title,
            Main,
            Description
        }
    }
</script>

<style>
    #app {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: black;
        margin-top: 40px;
        font-size: 16px;
        line-height: 1.5em;
    }
</style>
