Hey suyash here! again with a project but this time it is a QC project with NISQ hardware and noises !

Noise-Aware Quantum Circuit Layout Optimization Using Backend Calibration and Hybrid Fidelity–Depth Decision Metrics for NISQ Systems

Abstract
Noisy Intermediate-Scale Quantum (NISQ) processors exhibit strong qubit-to-qubit variability in coherence time, readout error, and gate fidelity, making circuit layout a primary determinant of execution accuracy. This work presents a calibration-driven quantum circuit layout optimizer that selects physical qubit mappings using backend noise parameters and transpilation depth analysis. The method extracts T1, T2, and readout error from hardware calibration data, constructs a qubit reliability score, constrains candidate layouts using device coupling maps, and evaluates routing cost through transpiled circuit depth. A hybrid decision metric combining reliability and depth is introduced to avoid performance degradation observed in naive noise-only mapping. Experiments using a Bell-state benchmark circuit under real backend noise models show measurable state degradation and demonstrate that reliability-only mapping increases circuit depth from 7 to 43 layers, whereas the proposed hybrid selector identifies balanced mappings with depth in the 13–30 range. The approach provides a practical, hardware-aware layout selection strategy aligned with current NISQ compilation research.

Index Terms
NISQ, quantum compilation, noise-aware optimization, qubit calibration, layout selection, transpilation depth, hybrid metric, Qiskit.

I. Introduction
Quantum program performance on NISQ hardware depends not only on circuit logic but also on the mapping between logical and physical qubits. Unlike classical processors, quantum devices exhibit heterogeneous qubit quality characterized by coherence variation, readout error, and gate error. Additionally, limited coupling graphs impose routing overhead, often introducing SWAP gates that increase circuit depth and decoherence exposure.


Standard transpilation pipelines optimize for connectivity and gate decomposition but do not always incorporate calibration-weighted qubit selection in a decision-theoretic manner. As a result, naive selection of high-quality qubits may paradoxically degrade performance if routing overhead increases significantly.
This work develops and evaluates a calibration-driven layout optimizer that integrates qubit reliability scoring, connectivity constraints, and transpilation depth into a hybrid layout decision engine. The objective is to produce a hardware-aware mapping strategy suitable for shallow and moderate-depth NISQ circuits.

II. Hardware Noise Model and Calibration Parameters
Each physical qubit is characterized by relaxation and dephasing parameters:
Energy relaxation time: T1


Phase coherence time: T2


Typical observed ranges on the tested backend were tens to hundreds of microseconds. Measurement reliability is characterized by readout error probability prp_rpr​, observed in the range of approximately 0.5%–5% across qubits.
Backend calibration data were accessed programmatically through the provider API and included:
per-qubit T1


per-qubit T2


readout error


coupling map graph


Noise simulation used a backend-derived noise model constructed from calibration parameters and applied through a density-matrix simulation method.




III. Reliability Scoring Model
A normalized qubit reliability score was defined to rank candidate qubits:
Sq​=​T1q​+T2q/1+pr​​
where:
T1q​ and T2q​ are coherence times


pr,qp​ is readout error probability


Observed score magnitudes for top qubits were on the order of:
Sq≈(3.8–4.5)×10−4S
Qubits were sorted in descending order of Sq​ to produce a reliability ranking.

IV. Connectivity-Constrained Candidate Selection
Physical feasibility requires that two-qubit gates operate only on connected qubit pairs. The device coupling map was modeled as an undirected graph G(V,E). Candidate layout pairs were restricted to edges (i,j)∈E(i,j) 
A connected-pair score was defined:
Spair(i,j)=Si+SjS
The highest-scoring connected pair represents the best reliability-only mapping candidate.

V. Benchmark Circuit and Experimental Setup
A two-qubit Bell-state circuit was used as a sensitivity benchmark:
Hadamard on qubit 0


Controlled-NOT (0 → 1)


Measurement


Ideal execution yields:
P(00)=0.5,P(11)=0.5
All experiments were run under three regimes:
Ideal state vector simulation


Generic noisy simulation


Backend-derived noise model simulation


Backend-derived noise simulation produced representative leakage:
Counts ≈ {00: 462, 11: 486, 01: 20, 10: 32}

indicating ~5% non-ideal outcomes.
Density matrix output (Fig. 1) showed reduced off-diagonal magnitude consistent with decoherence.

Fig. 1 — Noisy density matrix magnitude for Bell circuit under backend noise model.

VI. Routing Cost and Depth Measurement
Routing overhead was quantified using transpiled circuit depth:
D=depth(transpile(C,backend))
Baseline transpilation produced:
Default depth = 7

Reliability-only forced mapping produced:
Depth = 43

The increase was attributed to SWAP insertion due to layout distance.
This experimentally confirmed that reliability-only mapping is insufficient.

VII. Hybrid Fidelity–Depth Decision Metric
To balance noise quality and routing overhead, a hybrid metric was defined:
M(i,j)=Si+SjDi
where Di,jD
Algorithm:
Select top-K qubits by reliability


Enumerate connected pairs


Transpile circuit for each pair


Measure depth


Compute hybrid metric


Select maximum MMM


Example decision engine output:
Winner pair = (45, 1)
Depth = 30
Metric ≈ 3.19 × 10⁻⁵

VIII. Results
Observed layout performance:
Strategy
Depth
Default transpile
7
Reliability-only mapping
43
Depth-aware candidates
13–30

Error rates under noisy simulation showed that depth explosion correlated with increased output leakage, confirming routing depth as a dominant noise amplifier.
The hybrid selector avoided worst-case routing while preserving above-average qubit reliability.

IX. Discussion
Results show that:
Calibration-driven scoring alone is insufficient


Connectivity filtering is necessary but not sufficient


Routing depth must be included in the decision metric


Hybrid scoring aligns with compiler-level optimization principles


The method is computationally lightweight and suitable for shallow to moderate circuits.

X. Limitations and Future Work
Current implementation evaluates pairwise layouts only and uses circuit depth as a routing proxy. Future extensions include:
multi-qubit layout search


gate-error weighted scoring


integration with error mitigation


application to VQE/QAOA workloads


probabilistic routing cost models



XI. Conclusion
A calibration-driven, connectivity-constrained, depth-aware quantum circuit layout optimizer was implemented and experimentally validated. By combining qubit reliability metrics with transpilation depth in a hybrid decision function, the method avoids the failure modes of naive noise-only mapping and provides a practical hardware-aware layout selection strategy for NISQ systems.
The approach demonstrates that backend calibration data can be directly integrated into layout decisions, advancing quantum compilation toward adaptive, noise-resilient execution.

