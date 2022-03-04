Vue.component("problem-component", {
    props: {
        day: Number,
        title: String,
        p1Ans: String,
        p2Ans: String,
        input: {
            type: String,
            default: ""
        }
    },
    data() {
        return {
            stars: 0,
            ansChecker: "",
            saveName: "Buck4437_AoC_Lite_2021_stars"
        }
    },
    mounted() {
        document.title = `Day ${this.day} - Advent of Code Lite`;

        let data = this.getData();

        if (data[this.day]) {
            this.stars = data[this.day];
        }

        document.addEventListener("keydown", event => {
            if (event.code === "Enter") {
                this.submit();
            }
        });
    },
    computed: {
        hasInput() {
            return this.input.trim() !== "";
        }
    },
    watch: {
        stars(star) {
            let data = this.getData();
            data[this.day] = Math.max(star, data[this.day]|| 0);
            localStorage.setItem(this.saveName, JSON.stringify(data))
        }
    },
    methods: {
        getData() {
            try {
                return JSON.parse(localStorage.getItem(this.saveName)) || {};
            } catch(e) {
                return {};
            }
        },
        hide(...rest) {
            [...rest].forEach(n => this.$el.querySelector(n).classList.add("hidden"))
        },
        show(...rest) {
            [...rest].forEach(n => this.$el.querySelector(n).classList.remove("hidden"))
        },
        submit() {
            let ans = this.ansChecker.trim();
            if (ans === "") return;
            if (this.stars === 1 && ans === this.p2Ans) {
                this.stars = 2;
                alert("Your answer is correct! You have completed the problem!");
            } else if (this.stars === 0 && ans === this.p1Ans) {
                this.stars = 1;
                this.ansChecker = "";
                alert("Your answer is correct! Part 2 has been unlocked.");
            } else {
                alert("Your answer is incorrect.");
            }
        }
    },
    template: `
    <article>
        <h2>--- Day {{day}}: {{title}} ---</h2>

        <slot name="part1">Part 1 content</slot>
        <div v-if="stars === 0">
            <p v-if="hasInput">Your puzzle input is <span class="puzzle-input">{{input}}</span>.</p>
            <p v-else>To begin, <a class="link" href="./input.html" target="_blank">get your puzzle input</a>.</p>
        </div>

        <div v-if="stars > 0" class="part2">
            <p>Your puzzle answer was <code id="part1-ans-val">{{p1Ans}}</code>.</p>
            <p v-if="stars === 1"><em class="star">The first part of the puzzle is complete! It provides one gold star: *</em></p>
            <h2>--- Part Two ---</h2>
            <slot name="part2">Part 2 content</slot>

            <div v-if="stars === 1">
                <p v-if="hasInput">Your puzzle input is <span class="puzzle-input">{{input}}</span>.</p>
                <p v-else>Although it hasn't changed, you can still <a class="link" href="./input.html" target="_blank">get your puzzle input</a>.</p>
            </div>
        </div>

        <p v-if="stars < 2">Answer: <input class="input" v-model="ansChecker"><span class="link" id="submit" @click="submit">[Submit]</span></p>

        <div v-if="stars === 2">
            <p>Your puzzle answer was <code>{{p2Ans}}</code>.</p>
            <p><em class="star">Both parts of this puzzle are complete! They provide two gold stars: **</em></p>
            <p>At this point, you should <a class="link" href="../../index.html">return to your Advent calendar</a> and try another puzzle.</p>

            <p v-if="hasInput">Your puzzle input was <span class="puzzle-input">{{input}}</span>.</p>
            <p v-else>If you still want to see it, you can <a class="link" href="./input.html" target="_blank">get your puzzle input</a>.</p>
        </div>
    </article>`
})
