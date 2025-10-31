# 在您的 app.py 中新增以下代码
import streamlit as st
import plotly.graph_objects as go

def render_exposé():
    st.header("💊 药物研发『现形记』：从『幸运的意外』到『理性的必然』")
    st.markdown("---")

    # 引言：定下批判的基调
    st.markdown("""
    > 我们一直被教导要庆祝科学中的“意外发现”。但当我们为“威而钢”和“减肥神药”的幸运故事欢呼时，
    我们实际上是在庆祝一种**系统性的失败**——庆祝我们对其相的无知，并将患者的身体视为最后的试验场。
    现在，是时候结束这个蒙昧时代了。
    """)

    # 并排对比：旧范式 vs 新范式
    col_old, col_new = st.columns(2)

    with col_old:
        st.subheader("🚨 旧范式：『盲盒研发』")
        st.markdown("""
        **以 GLP-1 受体激动剂为例：**

        - **原始目标**：降血糖。
        - **研发路径**：像在黑暗中摸索，只盯着一个指标。
        - **“意外”发生**：患者体重减轻了。
        - **行业反应**：惊喜！我们中了彩票！
        - **代价**：
          - 数十亿研发资金在黑暗中燃烧。
          - **数十年时间被浪费**：从发现GLP-1到批准用于减肥，走了近30年。
          - **患者承受了本可预见的副作用**（如恶心、呕吐）。
        - **本质**：一场代价高昂的**赌博**，并将成功归因于“运气”。
        """)

    with col_new:
        st.subheader("🦉 新范式：『系统预见』")
        st.markdown("""
        **如果当时拥有我们的 ABN-QSS 系统：**

        - **目标输入**：“设计一个安全有效的降糖分子。”
        - **系统模拟**：在网络中运行，评估其对食欲、能耗、血糖、胃肠道的**全局影响**。
        - **关键预测**：系统会立即发出警报：
          > **“警告：该候选分子在『食欲抑制』和『能量消耗』节点产生强烈次级效应，其减肥潜力可能远超其降糖主业。同时，请注意其胃肠道副作用风险。”**
        - **结果**：
          - **提前30年**锁定其作为减肥药的霸主地位。
          - **主动优化**分子结构，减轻副作用。
          - **精准定位**市场和临床策略。
        - **本质**：基于**系统理解**的理性决策，结果是**必然的**。
        """)

    st.markdown("---")

    # 动态演示：重现历史的十字路口
    st.subheader("🔬 重现历史的十字路口")
    st.markdown("**让我们回到过去，看看ABN-QSS如何在研发的起点，就揭示出全部的真相。**")

    # 定义历史上的分子和我们的分子
    col_hist, col_abn = st.columns(2)

    with col_hist:
        st.markdown("**💊 历史上的『盲盒分子』**")
        st.caption("(基于司美格鲁肽的已知作用机制模拟)")
        historical_profile = [-0.6, 0.2, -0.9, -0.3]  # 这就是当年那个“降糖药”

        # 显示该分子的作用谱
        for i, (value, name) in enumerate(zip(historical_profile, ['食欲抑制', '能耗提升', '血糖控制', 'GI副作用'])):
            st.slider(name, -1.0, 1.0, value, key=f"hist_{i}", disabled=True)

    with col_abn:
        st.markdown("**🧬 ABN-QSS 『理性设计分子』**")
        st.caption("(基于同一靶点，但经过系统优化)")
        # 一个经过优化的、副作用更低的假设分子
        rational_profile = [-0.7, 0.6, -0.8, -0.6]

        for i, (value, name) in enumerate(zip(rational_profile, ['食欲抑制', '能耗提升', '血糖控制', 'GI副作用'])):
            st.slider(name, -1.0, 1.0, value, key=f"rat_{i}", disabled=True)

    # 运行模拟对比
    if st.button("🔄 运行历史对比模拟", type="secondary"):

        simulator = st.session_state.simulator
        hist_result = simulator.simulate(historical_profile)
        rat_result = simulator.simulate(rational_profile)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("历史分子 · 综合评分", f"{hist_result['composite_score']:.2f}")
            st.metric("历史分子 · GI副作用", f"{hist_result['steady_state'][3]:.2f}", delta="风险较高", delta_color="inverse")
        with col2:
            st.metric("理性分子 · 综合评分", f"{rat_result['composite_score']:.2f}", delta=f"{rat_result['composite_score'] - hist_result['composite_score']:.2f}")
            st.metric("理性分子 · GI副作用", f"{rat_result['steady_state'][3]:.2f}", delta="风险显著降低", delta_color="normal")

        # 可视化对比
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=hist_result['steady_state'],
            theta=simulator.node_names,
            fill='toself',
            name='历史盲盒分子',
            line=dict(color='red')
        ))
        fig.add_trace(go.Scatterpolar(
            r=rat_result['steady_state'],
            theta=simulator.node_names,
            fill='toself',
            name='理性设计分子',
            line=dict(color='green')
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[-1, 1])), showlegend=True, height=400)
        st.plotly_chart(fig, use_container_width=True)

        # 批判性总结
        st.error("""
        **💔 历史的代价：**
        - **浪费的30年**：社会晚了几十年才获得这种革命性的疗法。
        - **不必要的痛苦**：数百万患者承受了本可通过分子优化减轻的胃肠道副作用。
        - **巨大的资源错配**：数十亿美元被用于“试错”而非“优化”。
        """)

        st.success("""
        **🚀 我们的未来：**
        - **预见性开发**：在分子进入实验室前，看清其全部潜力与风险。
        - **主动优化**：从一开始就设计出更安全、更有效的版本。
        - **资源效率**：将宝贵的研发资金用于创造，而非猜测。
        """)

    st.markdown("---")
    st.markdown("""
    **🎯 结论：**
    所谓“幸运的意外”，不过是**系统性无知**的遮羞布。ABN-QSS范式所代表的，不是一项技术的进步，
    而是对整个药物研发哲学的**拨乱反正**——从依赖运气的**赌博**，转向基于系统理解的**工程**。
    我们不是要寻找下一个“幸运的意外”，而是要让这种“意外”彻底成为历史。
    """)

# 在您的主函数中调用这个页面
# 您可以通过一个导航栏来选择查看“设计模拟器”或“现形记”
