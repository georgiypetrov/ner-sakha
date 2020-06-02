<template>
    <div class="result">
        <p class="text-left">
            <template v-for="(word, index) in result.text">
                <template v-if="result.tags[index] === 'I-ORG' || result.tags[index] === 'B-ORG'">
                    <span v-bind:key="index" class="mr card redcard">{{word}} <span class="innertip">ORG</span></span>
                </template>
                <template v-else-if="result.tags[index] === 'I-LOC' || result.tags[index] === 'B-LOC'">
                    <span v-bind:key="index" class="mr card yellowcard">{{word}} <span class="innertip">LOC</span></span>
                </template>
                <template v-else-if="result.tags[index] === 'I-PER' || result.tags[index] === 'B-PER'">
                    <span v-bind:key="index" class="mr card greencard">{{word}} <span class="innertip">PER</span></span>
                </template>
                <template v-else>{{word}} </template>
            </template>
        </p>
    </div>
</template>

<script>
    export default {
        name: "Result",
        props: ['result']
    }
</script>

<style scoped>
    .result {
        border: 1px solid lightgray;
        border-radius: .25rem;
        padding: 20px;
        margin: 0 20px 20px 20px;
        width: 100%;
        background-color: white;
        line-height: 2rem;
    }

    .mr {
        margin-right: 5px;
    }

    .card {
        padding: .4em .4em;
        font-size: 75%;
        line-height: 1;
        text-align: center;
        white-space: nowrap;
        vertical-align: baseline;
        border-radius: .25rem;
        color: white;
        position: relative;
        display: inline-block;
    }

    .innertip {
        border: 1px solid white;
        padding: 2px 5px;
        font-size: 10px;
        margin-left: 5px;
    }

    .redcard {
        background-color: rgb(220, 53, 69);
    }

    .yellowcard {
        background-color: rgb(255, 193, 7);
    }

    .greencard {
        background-color: rgb(40, 167, 69);
    }
</style>