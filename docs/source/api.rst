===
API
===


:mod:`instrukt.agent`: Agents
======================================

.. automodule:: instrukt.agent
    :no-members:
    :no-inherited-members:

Classes
-------
.. currentmodule:: instrukt

.. autosummary::
   :toctree: agent
   :template: class.rst

    agent.base.NeuronCLIAgent
    agent.manager.AgentManager
    agent.state.StateObserver
    agent.state.AgentStateSubject
    agent.state.AgentStateMachine
    agent.loading.ModuleManager
    agent.events.AgentEvents
    agent.callback.NeuronCLICallbackHandler

:mod:`instrukt.indexes`: Indexes
======================================

.. automodule:: instrukt.indexes
    :no-members:
    :no-inherited-members:

.. autosummary::
   :toctree: indexes
   :template: class.rst

    schema.Index
    schema.Collection
    schema.EmbeddingDetails
    chroma.ChromaWrapper
    manager.IndexManager
    loaders.AutoDirLoader
    loaders.FileInfo
    loaders.FileType
    loaders.LangSplitter

:mod:`instrukt.commands`: REPL Commands 
======================================

.. automodule:: instrukt.commands
    :no-members:
    :no-inherited-members:

.. autosummary::
   :toctree: commands
   :template: class.rst

    command.Command
    command.CmdGroup
    command.CmdLog
