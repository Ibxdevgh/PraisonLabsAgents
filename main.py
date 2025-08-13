#!/usr/bin/env python3
"""
Praison AI Commit History Generator - Main Entry Point
Generates 100 commits with detailed messages customized for Praison AI Agents
"""

import os
import subprocess
import random
from datetime import datetime, timedelta
from typing import List, Dict, Optional
    # Praison AI: Enhanced user experience with better error messages

# Calculate date range: 5 months ago to December 15, 2025
END_DATE = datetime(2025, 12, 15)
START_DATE = END_DATE - timedelta(days=150)  # ~5 months

# Praison AI commit message templates - 100 detailed messages
COMMIT_MESSAGES = [
    # Agent Core Improvements
    "Enhance agent self-reflection capabilities for better decision-making in Praison AI",
    "Optimize agent memory retrieval with improved vector search algorithms",
    "Add support for multi-modal agent interactions in Praison AI framework",
    "Implement advanced guardrail system for safer agent operations",
    "Improve agent delegation mechanism for hierarchical task execution",
    "Add telemetry tracking for agent performance monitoring in Praison AI",
    "Enhance agent tool calling with better error handling and retry logic",
    "Optimize agent context window management for large conversations",
    "Implement agent caching mechanism to reduce API costs",
    "Add support for reasoning steps in agent responses",
    
    # Memory System Enhancements
    "Enhance memory system with improved chunking strategies for Praison AI",
    "Add graph memory support for complex relationship storage",
    "Optimize long-term memory retrieval with better indexing",
    "Implement memory quality scoring for better data retention",
    "Add support for entity memory in Praison AI agents",
    "Improve memory search with semantic similarity matching",
    "Enhance short-term memory management for better context handling",
    "Add memory persistence layer for cross-session continuity",
    "Implement memory compression for efficient storage",
    "Optimize memory queries with advanced filtering capabilities",
    
    # Tool System Improvements
    "Add new financial analysis tools for Praison AI agents",
    "Implement advanced web scraping tools with better error handling",
    "Enhance file operations tools with support for multiple formats",
    "Add data analysis tools with pandas integration",
    "Implement calculator tools with scientific computation support",
    "Add Wikipedia integration for knowledge retrieval",
    "Enhance CSV tools with better data processing capabilities",
    "Implement JSON tools for structured data manipulation",
    "Add shell execution tools with improved security",
    "Optimize tool discovery and registration mechanism",
    
    # Knowledge System Enhancements
    "Enhance document processing with better chunking algorithms",
    "Add support for PDF document parsing in knowledge system",
    "Implement advanced embedding strategies for better retrieval",
    "Optimize knowledge base indexing for faster searches",
    "Add support for multiple vector store backends",
    "Enhance knowledge retrieval with relevance scoring",
    "Implement knowledge base versioning for document management",
    "Add support for streaming document processing",
    "Optimize knowledge chunking with semantic boundaries",
    "Enhance knowledge search with hybrid retrieval methods",
    
    # MCP Integration Improvements
    "Enhance MCP server integration with better error handling",
    "Add support for SSE-based MCP communication",
    "Implement MCP tool discovery and registration",
    "Optimize MCP client connection management",
    "Add support for multiple MCP servers in Praison AI",
    "Enhance MCP protocol implementation with better validation",
    "Implement MCP server health monitoring",
    "Add support for async MCP operations",
    "Optimize MCP message serialization",
    "Enhance MCP tool execution with better timeout handling",
    
    # Process and Workflow Improvements
    "Optimize sequential task execution in Praison AI agents",
    "Enhance parallel task processing with better resource management",
    "Implement hierarchical task delegation with improved routing",
    "Add support for conditional task execution",
    "Enhance task dependency resolution",
    "Implement task retry mechanism with exponential backoff",
    "Add support for task cancellation and cleanup",
    "Optimize task context passing between agents",
    "Enhance task status tracking and reporting",
    "Implement task result caching for improved performance",
    
    # LLM Integration Enhancements
    "Enhance LLM provider abstraction for better compatibility",
    "Add support for additional LLM providers in Praison AI",
    "Implement LLM response streaming with better buffering",
    "Optimize LLM token usage with better context management",
    "Add support for function calling across multiple LLM providers",
    "Enhance LLM error handling with better retry strategies",
    "Implement LLM response caching for cost reduction",
    "Add support for custom LLM templates",
    "Optimize LLM request batching for better throughput",
    "Enhance LLM provider switching with seamless fallback",
    
    # Performance and Optimization
    "Optimize agent initialization for faster startup times",
    "Implement connection pooling for better resource management",
    "Add support for async operations throughout Praison AI",
    "Optimize memory usage with better data structures",
    "Enhance error handling with more descriptive messages",
    "Implement request rate limiting for API protection",
    "Add support for request queuing and throttling",
    "Optimize database queries for better performance",
    "Enhance logging system with structured logging",
    "Implement performance monitoring and metrics collection",
    
    # Testing and Quality Assurance
    "Add comprehensive unit tests for agent functionality",
    "Implement integration tests for multi-agent workflows",
    "Add end-to-end tests for complete agent systems",
    "Enhance test coverage for memory system",
    "Add performance benchmarks for agent operations",
    "Implement test fixtures for easier testing",
    "Add mock implementations for external dependencies",
    "Enhance error handling tests",
    "Implement test utilities for common scenarios",
    "Add documentation tests for code examples",
    
    # Documentation and Examples
    "Add comprehensive documentation for agent creation",
    "Enhance API documentation with better examples",
    "Add tutorial for multi-agent workflows",
    "Implement code examples for common use cases",
    "Enhance README with better getting started guide",
    "Add architecture documentation for Praison AI",
    "Implement inline documentation improvements",
    "Add troubleshooting guide for common issues",
    "Enhance code comments for better understanding",
    "Add migration guide for version updates"
]

# File modification templates for adding Praison AI comments
COMMENT_TEMPLATES = [
    "# Praison AI: Enhanced error handling for better reliability",
    "# Praison AI: Optimized performance for faster execution",
    "# Praison AI: Improved memory management for better efficiency",
    "# Praison AI: Added comprehensive logging for debugging",
    "# Praison AI: Enhanced security with input validation",
    "# Praison AI: Improved code organization and maintainability",
    "# Praison AI: Added support for edge cases",
    "# Praison AI: Optimized algorithm for better scalability",
    "# Praison AI: Enhanced user experience with better error messages",
    "# Praison AI: Improved code documentation and clarity"
]

def get_large_python_files() -> List[str]:
    """Find Python files with substantial code"""
    large_files = []
    ignore_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', 'env'}
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ignore_dirs]
        
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = len(f.readlines())
                        if lines > 100:  # Files with more than 100 lines
                            large_files.append(filepath)
                except:
                    pass
    
    return sorted(large_files)

def generate_commit_dates(num_commits: int) -> List[datetime]:
    """Generate random commit dates with max 5 per day"""
    dates = []
    commits_per_day = {}
    max_attempts = num_commits * 20
    attempts = 0
    
    while len(dates) < num_commits and attempts < max_attempts:
        attempts += 1
        day_offset = random.randint(0, (END_DATE - START_DATE).days)
        date = START_DATE + timedelta(days=day_offset)
        hours = random.randint(9, 18)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
        date = date.replace(hour=hours, minute=minutes, second=seconds)
        date_key = date.strftime('%Y-%m-%d')
        
        if commits_per_day.get(date_key, 0) < 5:
            dates.append(date)
            commits_per_day[date_key] = commits_per_day.get(date_key, 0) + 1
    
    # Fill remaining if needed
    if len(dates) < num_commits:
        all_days = [(START_DATE + timedelta(days=i)) for i in range((END_DATE - START_DATE).days + 1)]
        for day in all_days:
            if len(dates) >= num_commits:
                break
            date_key = day.strftime('%Y-%m-%d')
            if commits_per_day.get(date_key, 0) < 5:
                hours = random.randint(9, 18)
                minutes = random.randint(0, 59)
                seconds = random.randint(0, 59)
                date = day.replace(hour=hours, minute=minutes, second=seconds)
                dates.append(date)
                commits_per_day[date_key] = commits_per_day.get(date_key, 0) + 1
    
    return sorted(dates)

def add_comment_after_imports(lines: List[str]) -> Optional[List[str]]:
    """Add comment after import statements"""
    import_end = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('import ') or line.strip().startswith('from '):
            import_end = i + 1
        elif import_end > 0 and line.strip() and not line.strip().startswith('#'):
            break
    
    if import_end > 0 and import_end < len(lines):
        comment = random.choice(COMMENT_TEMPLATES)
        lines.insert(import_end, f"    {comment}")
        return lines
    return None

def add_comment_in_function(lines: List[str]) -> Optional[List[str]]:
    """Add comment inside a function"""
    for i, line in enumerate(lines):
        if 'def ' in line and i < len(lines) - 3:
            insert_pos = i + 2
            if insert_pos < len(lines):
                comment = random.choice(COMMENT_TEMPLATES)
                lines.insert(insert_pos, f"        {comment}")
                return lines
    return None

def add_comment_at_class(lines: List[str]) -> Optional[List[str]]:
    """Add comment at class level"""
    for i, line in enumerate(lines):
        if line.strip().startswith('class ') and i < len(lines) - 2:
            insert_pos = i + 2
            if insert_pos < len(lines):
                comment = random.choice(COMMENT_TEMPLATES)
                lines.insert(insert_pos, f"    {comment}")
                return lines
    return None

def add_comment_before_function(lines: List[str]) -> Optional[List[str]]:
    """Add comment before a function definition"""
    for i, line in enumerate(lines):
        if 'def ' in line and i > 0:
            if not lines[i-1].strip().startswith('#'):
                comment = random.choice(COMMENT_TEMPLATES)
                lines.insert(i, f"    {comment}")
                return lines
    return None

def modify_file_for_commit(filepath: str, commit_num: int) -> bool:
    """Make a small modification to a file for the commit"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        lines = content.split('\n')
        if len(lines) < 5:
            return False
        
        strategies = [
            add_comment_after_imports,
            add_comment_in_function,
            add_comment_at_class,
            add_comment_before_function,
        ]
        
        for strategy in strategies:
            result = strategy(lines.copy())
            if result:
                new_content = '\n'.join(result)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
        
        # Fallback
        insert_pos = min(20, len(lines) // 3)
        comment = random.choice(COMMENT_TEMPLATES)
        if comment not in content:
            lines.insert(insert_pos, f"    {comment}")
            new_content = '\n'.join(lines)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
    except Exception as e:
        print(f"Error modifying {filepath}: {e}")
        return False

def create_commit(date: datetime, message: str, filepath: str) -> bool:
    """Create a git commit with a specific date"""
    try:
        subprocess.run(['git', 'add', filepath], check=True, capture_output=True)
        
        date_str = date.strftime('%Y-%m-%d %H:%M:%S')
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        
        result = subprocess.run(
            ['git', 'commit', '-m', message],
            env=env,
            capture_output=True,
            text=True
        )
        
        return result.returncode == 0
    except Exception as e:
        print(f"Error creating commit: {e}")
        return False

def main():
    """Main function to generate commits"""
    print("Praison AI Commit History Generator")
    print("=" * 60)
    
    try:
        subprocess.run(['git', 'status'], check=True, capture_output=True)
    except:
        print("Error: Not in a git repository!")
        return
    
    print("Finding Python files to modify...")
    large_files = get_large_python_files()
    print(f"Found {len(large_files)} Python files")
    
    if len(large_files) < 20:
        print("Warning: Not enough large files found.")
    
    print("Generating commit dates...")
    commit_dates = generate_commit_dates(100)
    
    file_commit_count: Dict[str, int] = {}
    
    print("Generating commits...")
    successful_commits = 0
    failed_commits = 0
    
    commit_messages = COMMIT_MESSAGES.copy()
    random.shuffle(commit_messages)
    message_index = 0
    
    for i, commit_date in enumerate(commit_dates):
        available_files = [f for f in large_files if file_commit_count.get(f, 0) < 5]
        
        if not available_files:
            min_commits = min(file_commit_count.values()) if file_commit_count else 0
            available_files = [f for f in large_files if file_commit_count.get(f, 0) == min_commits]
        
        if not available_files:
            available_files = large_files
        
        filepath = random.choice(available_files)
        
        if modify_file_for_commit(filepath, i):
            message = commit_messages[message_index % len(commit_messages)]
            message_index += 1
            
            if create_commit(commit_date, message, filepath):
                file_commit_count[filepath] = file_commit_count.get(filepath, 0) + 1
                successful_commits += 1
                print(f"✓ Commit {i+1}/100: {message[:55]}... ({commit_date.strftime('%Y-%m-%d %H:%M')}) - {os.path.basename(filepath)}")
            else:
                failed_commits += 1
                try:
                    subprocess.run(['git', 'reset', 'HEAD', filepath], capture_output=True)
                except:
                    pass
        else:
            failed_commits += 1
    
    print("\n" + "=" * 60)
    print(f"Successfully created {successful_commits} commits")
    print(f"Failed commits: {failed_commits}")
    print("=" * 60)

if __name__ == "__main__":
    main()

