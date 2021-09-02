import msprime
import numpy as np
import tskit

dem = msprime.Demography.from_species_tree("((A:900,B:900)ab:100,C:1000)abc;", initial_size=1e3)
samples = {"A": 20, "B": 20, "C":20}  # take 20 diploids from terminal populations A, B, C
ts_full = msprime.sim_ancestry(
   samples, demography=dem, sequence_length=5e4, recombination_rate=1e-8, random_seed=1234
)
first_4_nodes = [0, 1, 2, 3]  # ids of the first 4 sample nodes (here, 2 individuals from A)
eight_nodes = first_4_nodes + [40, 41, 80, 81]  # Add nodes from individuals in B & C
ts_tiny = ts_full.simplify(first_4_nodes)  # a tiny 4-tip TS
ts_small = ts_full.simplify(eight_nodes)   # a small 8-tip TS

ts_mutated = msprime.sim_mutations(ts_small, rate=1e-7, random_seed=7)


x_limits = [1000, 6000]

nd_labels = {}  # An array of labels for the nodes
for n in ts_mutated.nodes():
    # Set sample node labels from metadata. Here we use the population name, but you might want
    # to use the *individual* name instead, if the individuals in your tree sequence have names
    if n.is_sample():
        nd_labels[n.id] = ts_mutated.population(n.population).metadata["name"]

mut_labels = {}  # An array of labels for the mutations
for mut in ts_mutated.mutations():  # Make pretty labels showing the change in state
    site = ts_mutated.site(mut.site)
    older_mut = mut.parent >= 0  # is there an older mutation at the same position?
    prev = ts_mutated.mutation(mut.parent).derived_state if older_mut else site.ancestral_state
    mut_labels[mut.id] = "{}→{}".format(prev, mut.derived_state)

SVG(ts_mutated.draw_svg(
        x_lim=x_limits,
        node_labels=nd_labels,
        mutation_labels=mut_labels,
        size=(1000,400),
        path="../figs/mutated_trees.svg",
    ))

SVG(ts_full.draw_svg(
    x_lim=[0, 2000],
    node_labels={},
    size=(400, 400),
    path="../figs/plain_ts.svg"
))

mts = msprime.sim_mutations(ts_full, rate=1e-7, random_seed=123)

mut_labels = {}  # An array of labels for the mutations
for mut in ts_mutated.mutations():  # Make pretty labels showing the change in state
    site = ts_mutated.site(mut.site)
    older_mut = mut.parent >= 0  # is there an older mutation at the same position?
    prev = ts_mutated.mutation(mut.parent).derived_state if older_mut else site.ancestral_state
    mut_labels[mut.id] = "{}→{}".format(prev, mut.derived_state)
SVG(mts.draw_svg(
    x_lim=[0, 2000],
    node_labels={},
    mutation_labels=mut_labels,
    size=(400, 400),
    path="../figs/mutated_ts.svg"
))

alleles = ["💩", "🎄", "🔥"]
model = msprime.MatrixMutationModel(
    alleles,
    root_distribution = [0.0, 1.0, 0.0],
    transition_matrix = [[0.0, 1.0, 0.0],
                         [0.0, 0.2, 0.8],
                         [1.0, 0.0, 0.0]]
)
ts = msprime.sim_ancestry(5, population_size=1e4, recombination_rate=1e-8, sequence_length=1000, random_seed=9)
mts = msprime.sim_mutations(ts, rate=5e-8, model=model, random_seed=1)

SVG(mts.draw_svg(
        size=(400,500),
        node_labels={},
        mutation_labels={m.id: m.derived_state for m in mts.mutations()},
        symbol_size=10,
        force_root_branch=True,
        path="../figs/fire_trees.svg",
    ))


sweep_model = msprime.SweepGenicSelection(position=2.5e4,
    s=0.01, start_frequency=0.5e-4, end_frequency=0.99, dt=1e-6)
sts = msprime.sim_ancestry(9,
    model=[sweep_model, msprime.StandardCoalescent()],
    population_size=1e4,
    recombination_rate=1e-8,
    sequence_length=5e4, random_seed=9,
)

def sel_svg(**kwargs):
    return sts.draw_svg(
        size=(1000,400),
        x_lim=[2e4, 3e4],
        node_labels={},
        symbol_size=10,
        force_root_branch=True,
        **kwargs
    )
    
SVG(sel_svg())

sel_svg(path="../figs/sweep_trees.svg");

ots = msprime.sim_ancestry(9,
    model=sweep_model,
    population_size=1e4,
    recombination_rate=1e-8,
    sequence_length=5e4, random_seed=9,
)
SVG(ots.draw_svg(
    x_lim=[2.2e4, 2.6e4],
    size=(400,140),
    node_labels={},
    path="../figs/pre_recap.svg"
))

rts = msprime.sim_ancestry(
    initial_state=ots,
    recombination_rate=1e-8,
    population_size=1e4,
    random_seed=10
)
SVG(rts.draw_svg(
    x_lim=[2.2e4, 2.6e4],
    size=(400,500),
    node_labels={},
    path="../figs/post_recap.svg"
))
